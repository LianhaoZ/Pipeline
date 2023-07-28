# Copyright 2016-2023 The Van Valen Lab at the California Institute of
# Technology (Caltech), with support from the Paul Allen Family Foundation,
# Google, & National Institutes of Health (NIH) under Grant U24CA224309-01.
# All rights reserved.
#
# Licensed under a modified Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.github.com/vanvalenlab/deepcell-tf/LICENSE
#
# The Work provided may be used for non-commercial academic purposes only.
# For any other use of the Work, including commercial use, please contact:
# vanvalenlab@gmail.com
#
# Neither the name of Caltech nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific
# prior written permission.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""A model that can detect whether 2 cells are same, different, or related."""


import os

import tensorflow as tf

import deepcell_tracking

from deepcell.applications import Application


MODEL_PATH = ('https://deepcell-data.s3-us-west-1.amazonaws.com/'
              'saved-models/NuclearTrackingInf-75.tar.gz')
MODEL_HASH = '5dbd8137be851a0c12557fcde5021444'

ENCODER_PATH = ('https://deepcell-data.s3-us-west-1.amazonaws.com/'
                'saved-models/NuclearTrackingNE-75.tar.gz')
ENCODER_HASH = 'a466682c9d1d5e3672325bb8a13ab3e0'

MODEL_METADATA = {
    'batch_size': 8,
    'n_layers': 1,
    'graph_layer': 'gat',
    'epochs': 50,
    'steps_per_epoch': 1000,
    'validation_steps': 200,
    'rotation_range': 180,
    'translation_range': 512,
    'buffer_size': 128,
    'n_filters': 64,
    'embedding_dim': 64,
    'encoder_dim': 64,
    'lr': .001,
    'data_fraction': 1,
    'norm_layer': 'batch',
    'appearance_dim': 32,
    'distance_threshold': 64,  #ewewew
    'crop_mode': 'resize',
}

DISTANCE_THRESHOLD = 64   #ewewew
APPEARANCE_DIM = 32 
CROP_MODE = 'resize'
NORM = True
BIRTH = 0.99
DEATH = 0.99
DIVISION = 0.01
TRACK_LENGTH = 8
MODEL_MPP = 0.65


class CellTracking(Application):
    """Loads a :mod:`deepcell.model_zoo.tracking.GNNTrackingModel` model for
    object tracking with pretrained weights using a simple
    ``predict`` interface.

    Args:
        use_pretrained_weights (bool): Whether to load pretrained weights.
        model_image_shape (tuple): Shape of input data expected by model.
        neighborhood_scale_size (int): Size of the area surrounding each cell.
        birth (float): Cost of new cell in linear assignment matrix.
        death (float): Cost of cell death in linear assignment matrix.
        division (float): Cost of cell division in linear assignment matrix.
    """

    #: Metadata for the dataset used to train the model
    dataset_metadata = {
        'name': 'tracked_nuclear_train_large',
        'other': 'Pooled tracked nuclear data from HEK293, HeLa-S3, NIH-3T3, and RAW264.7 cells.'
    }

    #: Metadata for the model and training process
    model_metadata = MODEL_METADATA

    def __init__(self,
                 model=None,
                 neighborhood_encoder=None,
                 distance_threshold=DISTANCE_THRESHOLD,
                 appearance_dim=APPEARANCE_DIM,
                 birth=BIRTH,
                 death=DEATH,
                 division=DIVISION,
                 track_length=TRACK_LENGTH,
                 embedding_axis=0,
                 crop_mode=CROP_MODE,
                 norm=NORM):
        self.neighborhood_encoder = neighborhood_encoder
        self.distance_threshold = distance_threshold
        self.appearance_dim = appearance_dim
        self.birth = birth
        self.death = death
        self.division = division
        self.track_length = track_length
        self.embedding_axis = embedding_axis
        self.crop_mode = crop_mode
        self.norm = norm
        
        if self.neighborhood_encoder is None:
            archive_path = tf.keras.utils.get_file(
                'NuclearTrackingNE.tgz', ENCODER_PATH,
                file_hash=ENCODER_HASH,
                extract=True, cache_subdir='models')
            model_path = os.path.splitext(archive_path)[0]
            self.neighborhood_encoder = tf.keras.models.load_model(model_path)

        if model is None:
            archive_path = tf.keras.utils.get_file(
                'NuclearTrackingInf.tgz', MODEL_PATH,
                file_hash=MODEL_HASH,
                extract=True, cache_subdir='models')
            model_path = os.path.splitext(archive_path)[0]
            model = tf.keras.models.load_model(model_path)

        super().__init__(
            model,
            model_mpp=MODEL_MPP,
            preprocessing_fn=None,
            postprocessing_fn=None,
            dataset_metadata=self.dataset_metadata,
            model_metadata=self.model_metadata)

    def predict(self, image, labels, **kwargs):
        """Using both raw image data and segmentation masks,
        track objects across all frames.

        Args:
            image (numpy.array): Raw image data.
            labels (numpy.array): Labels for ``image``, integer masks.

        Returns:
            dict: Tracked labels and lineage information.
        """
        print(self.distance_threshold)
        print(self.division)
        cell_tracker = deepcell_tracking.CellTracker(
            image,
            labels,
            self.model,
            neighborhood_encoder=self.neighborhood_encoder,
            distance_threshold=self.distance_threshold,
            appearance_dim=self.appearance_dim,
            track_length=self.track_length,
            embedding_axis=self.embedding_axis,
            birth=self.birth,
            death=self.death,
            division=self.division,
            crop_mode=self.crop_mode,
            norm=self.norm)

        cell_tracker.track_cells()

        return cell_tracker._track_review_dict()


    def track(self, image, labels, **kwargs):
        """Wrapper around predict() for convenience."""
        return self.predict(image, labels, **kwargs)

 