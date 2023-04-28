import numpy as np
import skimage
from skimage import measure
import os 
from PIL import Image

# Set the directory path
dir_path = "/Users/lian/Desktop/Cellpose/First10" 
  
# Loop through all files in the directory
for file_name in os.listdir(dir_path):
    # Check if the file is a TIF image
    if file_name.endswith(".tif"):

        labeled_image = skimage.io.imread(os.path.join(dir_path, file_name))
        # Load the labeled image
        # labeled_image = np.load(os.path.join(dir_path, file_name), allow_pickle=True)
   
        # Find the properties of the labeled objects
        label_properties = measure.regionprops(labeled_image)

        # Print the properties of the first object
        print('Label:', label_properties[0].label)
        print('Centroid:', label_properties[0].centroid)
        print('Bounding box:', label_properties[0].bbox)
        print('Area:', label_properties[0].area)
        print('Perimeter:', label_properties[0].perimeter)
