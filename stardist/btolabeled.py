from skimage.measure import label
from skimage import io
import numpy as np
import os

file_path = "/Users/lian/Desktop/stardist/GT/man_seg105.tif"
# file_path = "/Users/lian/Desktop/stardist/Quest-seg/masks/seg_run_DAPI_XY105_T01.tif"
output_path = "/Users/lian/Desktop/stardist/GT/105.tif"
# output_path = "/Users/lian/Desktop/stardist/Quest-seg/masks/srun_DAPI_XY105_T01.tif"
img = io.imread(file_path)

img = label(img)
img = img.astype(np.uint16)

io.imsave(output_path, img, plugin='tifffile')
os.remove(file_path)



# # convert binary files in a folder to labeled
# folderpath = "/Users/lian/Desktop/stardist/Quest-seg/masks/"
# output_folder = "/Users/lian/Desktop/stardist/GT/Labeledsd/"
# array = ["seg_run_DAPI_XY015_T01.tif","seg_run_DAPI_XY064_T01.tif", "seg_run_DAPI_XY115_T01.tif"]
# for file_name in os.listdir(folderpath):
#     if file_name in array:
#         file_path = os.path.join(folderpath, file_name)
#         img = io.imread(file_path)

#         img = label(img)
#         img = img.astype(np.uint16)
#         outputpath = os.path.join(output_folder, file_name)
#         io.imsave(outputpath, img, plugin='tifffile')


