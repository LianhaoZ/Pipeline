import os
import numpy as np
from skimage import io
from deepcell_tracking import CellTracker
from deepcell.model_zoo.tracking import GNNTrackingModel
tm = GNNTrackingModel()

import numpy as np
from tifffile import imread

def tif_to_nparray(filepath):
    # Read the TIF file
    tif_data = imread(filepath)

    # Convert the TIF data to a NumPy array
    np_array = np.array(tif_data)

    return np_array

folder_path = '/Users/lian/Desktop/Tracking/Deepcell/Trial_run/Raw(5)Images.tif'
 
# raw image array
y = tif_to_nparray(folder_path) 
y1 = y[..., np.newaxis]  

folder_path1 = '/Users/lian/Desktop/Tracking/Deepcell/Trial_run/Segmented(5).tif'
 

# segmented image array 
X = tif_to_nparray(folder_path1)
X1 = X[..., np.newaxis]  

# X and y are the time-sequence data and their corresponding segmentations (labels), respectively.
# model is a deepcell-tf tracking model. 
tracker = CellTracker(movie=y1, annotation=X1, neighborhood_encoder=tm.neighborhood_encoder, tracking_model=tm.inference_model)

tracker.track_cells()  # runs in place, builds tracks
 
# # /////// View results #

# # View tracked results of each batch as a video
# # NB: This does not render well on GitHub
# from IPython.display import HTML
# from deepcell.utils.plot_utils import get_js_video

# # Raw
# HTML(get_js_video(np.expand_dims(y1, axis=0),
#                   batch=0, cmap='gray'))

# # Tracked

# # Scale the colors to match the max cell label
# HTML(get_js_video(np.expand_dims(tracker.y_tracked, axis=0),
#                   batch=0, cmap='cubehelix', vmin=0,
#                   vmax=len(tracker.tracks)))

# # ///////

# # Save all tracked data and lineage files to a .trk file
tracker.dump('./results.trk')

# # Open the track file
# from deepcell_tracking.utils import load_trks

# data = load_trks('./results.trk')

# lineage = data['lineages']  # linage information
# X = data['X']  # raw X data
# y = data['y']  # tracked y data

import imageio
from matplotlib import pyplot as plt
OUTPUT_DIR = '/Users/lian/Desktop/Tracking/Deepcell/Trial_run'
vmax = len(tracker.y_tracked)

raw = []
tracked = []

for i in range(tracker.X.shape[0]):
    new_image = tracker.X[i, ..., 0]
    raw_path = os.path.join(OUTPUT_DIR, 'image_%d.tiff' % i)
    imageio.imwrite(raw_path, new_image.astype('uint8'))
    raw.append(new_image.astype('uint8'))

    label_image = tracker.y_tracked[i, ..., 0].astype('uint8')
    label_path = os.path.join(OUTPUT_DIR, 'label_%d.tiff' % i)
    plt.imsave(label_path, label_image,
               cmap='cubehelix', vmin=0, vmax=vmax)
    # imageio.imwrite(label_path, label_image,
    #                 cmap='cubehelix', vmin=0, vmax=vmax)
    tracked.append(label_image.astype('uint8'))

# Make gifs
imageio.mimsave(os.path.join(OUTPUT_DIR, 'raw.gif'), raw)
imageio.mimsave(os.path.join(OUTPUT_DIR, 'tracked.gif'), tracked)