import os
import json

import btrack
import napari

import numpy as np
import pandas as pd

from skimage import io
from napari.utils import nbscreenshot

from btrack import datasets

# example segmentation
segmentation = datasets.example_segmentation()

# example config
config = datasets.cell_config()

# example objects
objects = datasets.example_track_objects()

# objects = btrack.dataio.import_CSV('napari_example.csv')

# initialise a tracker session using a context manager
with btrack.BayesianTracker() as tracker:

  # configure the tracker using a config file
  tracker.configure_from_file('./config.json')

  # append the objects to be tracked
  tracker.append(objects)

  # set the volume (Z axis volume is set very large for 2D data)
  tracker.volume=((0,1600), (0,1200), (-1e5,1e5))

  # track them (in interactive mode)
  tracker.track_interactive(step_size=100)

  # generate hypotheses and run the global optimizer
  tracker.optimize()

  # get the tracks in a format for napari visualization
  data, properties, graph = tracker.to_napari(ndim=2)

vertices = data[:, 1:]

stack = io.imread('/Users/lian/Desktop/Tracking/Trackmate7/11/segmented-imgs.tif')

with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(stack)
    viewer.add_points(vertices, size=4, name='points', opacity=0.3)
    viewer.add_tracks(data, properties=properties, graph=graph, name='tracks')