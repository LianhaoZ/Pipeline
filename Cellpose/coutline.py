from cellpose import io, utils 
import os
import skimage
import numpy as np
string = ["010","013","015", "035", "043", "052", "064", "105","110", "115", "113"]

for i in string: 
        
    # Directory containing the Raw images
    image_name = f'/Users/lian/Desktop/Checking Seg/run_DAPI_XY{i}_T01.tif'
    # Directory containing the Mask images
    masks = skimage.io.imread(f'/Users/lian/Desktop/Checking Seg/run_DAPI_XY{i}_T01_cp_masks.tif')  
    
    # image_name is file name of image
    # masks is numpy array of masks for image
    base = os.path.splitext(image_name)[0] 
    outlines = utils.outlines_list(masks)
    io.outlines_to_text(base, outlines)