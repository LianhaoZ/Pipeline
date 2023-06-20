import os
import numpy as np
from skimage import io
# from deepcell_tracking import CellTracker
# from deepcell.model_zoo.tracking import GNNTrackingModel
# tm = GNNTrackingModel()
from deepcell.applications.cell_tracking import CellTracking

from tifffile import imread

OUTPUT_DIR = '/Users/lian/Desktop/Tracking/Deepcell/Trial_run'

# (raw image)
folder_path = '/Users/lian/Desktop/Tracking/Trackmate7/11/Raw-images.tif'

# (segmented image)
folder_path1 = '/Users/lian/Desktop/Tracking/Trackmate7/11/segmented-imgs.tif'

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
Tracking = CellTracking(model=None, neighborhood_encoder=None, distance_threshold=64, appearance_dim=32, birth=0.99, death=0.99, division=0.01, track_length=8, embedding_axis=0, crop_mode='resize', norm=True)
Dict = Tracking.predict(image = y1, labels = X1)

# print(Dict.keys()) 
 
# # # # /////// View results  in HTML /////// # # # 

# # View tracked results of each batch as a video
# # NB: This does not render well on GitHub
# from IPython.display import HTML
# from deepcell.utils.plot_utils import get_js_video
# from IPython.display import display

# # Tracked

# # Scale the colors to match the max cell label
# html = get_js_video(np.expand_dims(Dict['y'], axis=0),
#                   batch=0, cmap='cubehelix', vmin=0,
#                   vmax=len(Dict['tracks']))
# html_filename = 'output1.html'
# with open(html_filename, 'w') as file:
#     file.write(html)


# import imageio

# def convert_dict_to_tifs(data_dict, output_directory):
#     # Set the output file name
#     output_file = 'movie.tiff'

#     # Create an empty list to store the image frames
#     frames = []

#     # Iterate over the frames in the dictionary
#     for frame_index, frame_data in data_dict.items():
#         width = frame_data['width']
#         height = frame_data['height']
#         pixels = frame_data['pixels']

#         # Create an image object using Pillow
#         image = Image.fromarray(np.array(pixels, dtype=np.uint8))

#         # Append the image to the frames list
#         frames.append(image)

#     # Save the frames as a TIFF movie using imageio
#     imageio.mimwrite(output_file, frames, format='TIFF', fps=10)

 
# convert_dict_to_tifs(Dict, output_directory)

# print("Done", Dict['y'].shape)

# # # # /////// Access as gif /////// # # # 

# from matplotlib import pyplot as plt
# import imageio

# vmax = len(Dict["y"])

# # raw = []
# tracked = []

# for i in range(Dict["X"].shape[0]):
#     # new_image = Dict["X"][i, ..., 0]
#     # raw_path = os.path.join(OUTPUT_DIR, 'image_%d.tiff' % i)
#     # imageio.imwrite(raw_path, new_image.astype('uint8'))
#     # raw.append(new_image.astype('uint8'))

#     label_image = Dict["y"][i, ..., 0].astype('uint8')
#     label_path = os.path.join(OUTPUT_DIR, 'label_%d.tiff' % i)
#     plt.imsave(label_path, label_image,
#                cmap='cubehelix', vmin=0, vmax=vmax)
#     # imageio.imwrite(label_path, label_image,
#     #                 cmap='cubehelix', vmin=0, vmax=vmax)
#     tracked.append(label_image.astype('uint8'))

# # Make gifs
# # imageio.mimsave(os.path.join(OUTPUT_DIR, 'raw.gif'), raw)
# imageio.mimsave(os.path.join(OUTPUT_DIR, 'tracked.gif'), tracked)

# # # # /////// Access as CSV /////// # # # 

import csv
  
# Specify the output CSV file path
output_file = 'data.csv'

# Extract keys and values from the dictionary
# keys = list(Dict.keys()[1:])
# values = list(Dict.values()[1:])
keys = Dict["tracks"].values()
values = Dict["tracks"].values()
# print(tracks)
# for i in keys:
#     print(type(Dict[i]))
  

# Write the dictionary data to a CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(keys)
    writer.writerow(values)