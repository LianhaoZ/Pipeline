from fix import CellTracking
import os
import numpy as np
from skimage import io 
# from deepcell.applications.cell_tracking import CellTracking
from tifffile import imread
import csv 
import tifffile 
from deepcell_tracking.utils import get_max_cells
from deepcell_tracking.utils import normalize_adj_matrix
from deepcell_tracking.utils import get_image_features
import pandas 
from scipy.spatial.distance import cdist
OUTPUT_DIR = '/Users/lian/Desktop'


dt = 64

# (raw image)
# folder_path = '/Users/lian/Desktop/XY001.tif'
folder_path = '/Users/lian/Desktop/XY001.tif'

# (segmented image)
# folder_path1 = '/Users/lian/Desktop/masks1.tif'
folder_path1 = '/Users/lian/Desktop/masks1.tif'

def tif_to_nparray(filepath):
    # Read the TIF file
    tif_data = imread(filepath)

    # Convert the TIF data to a NumPy array
    np_array = np.array(tif_data)

    return np_array
 
# raw image array
y = tif_to_nparray(folder_path) 
y1 = y[..., np.newaxis]  

print("raw image converted", y1.shape)  

# segmented image array 
X = tif_to_nparray(folder_path1)
X1 = X[..., np.newaxis]  

print("segmented image converted", X1.shape)
# Tracking = CellTracking(model=None, neighborhood_encoder=None, distance_threshold=64, appearance_dim=32, birth=0.99, death=0.99, division=0.01, track_length=8, embedding_axis=0, crop_mode='resize', norm=True)
# ^above is default parameters of the Tracker
# tracker = CellTracking(distance_threshold=128,division=0.9,track_length=5)
tracker = CellTracking(distance_threshold = 128)
tracked_data = tracker.predict(y1, X1)
y_tracked = tracked_data['y_tracked']

tifffile.imsave(OUTPUT_DIR+"/test-num1-128meta.tif", y_tracked)



# movie = y1
# label = X1 
# max_cells = get_max_cells(label)
# n_frames = movie.shape[0]

# centroids = np.zeros((n_frames, max_cells, 2), dtype=np.float32)

# adj_matrix = np.zeros((n_frames, max_cells, max_cells), dtype=np.float32)
# print(adj_matrix)
# for frame in range(n_frames):
#     frame_features = get_image_features(movie[frame].astype(int), label[frame].astype(int), crop_mode='resize', norm=True)

#     # for cell_idx, cell_id in enumerate(frame_features['labels']):
#     #     self.id_to_idx[cell_id] = cell_idx
#     #     self.idx_to_id[(frame, cell_idx)] = cell_id

#     num_tracks = len(frame_features['labels'])
#     centroids[frame, :num_tracks] = frame_features['centroids'] 
#     # appearances[frame, :num_tracks] = frame_features['appearances']

#     cent = centroids[frame]
#     distance = cdist(cent, cent, metric='euclidean') < dt
#     adj_matrix[frame] = distance.astype('float32')

#     # Normalize adj matrix
#     norm_adj_matrices = normalize_adj_matrix(adj_matrix)
        
# print(adj_matrix)
# tifffile.imsave(OUTPUT_DIR+"/adj-1.tif", adj_matrix)



# dt = 128

# for frame in range(n_frames):
#     frame_features = get_image_features(movie[frame].astype(int), label[frame].astype(int), crop_mode='resize', norm=True)

#     # for cell_idx, cell_id in enumerate(frame_features['labels']):
#     #     self.id_to_idx[cell_id] = cell_idx
#     #     self.idx_to_id[(frame, cell_idx)] = cell_id

#     num_tracks = len(frame_features['labels'])
#     centroids[frame, :num_tracks] = frame_features['centroids'] 
#     # appearances[frame, :num_tracks] = frame_features['appearances']

#     cent = centroids[frame]
#     distance = cdist(cent, cent, metric='euclidean') < dt
#     adj_matrix[frame] = distance.astype('float32')

#     # Normalize adj matrix
#     norm_adj_matrices = normalize_adj_matrix(adj_matrix)


# print(adj_matrix)
# tifffile.imsave(OUTPUT_DIR+"/adj-2.tif", adj_matrix)