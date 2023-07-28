import argparse
import os 
from stardist.models import StarDist2D 
from stardist.plot import render_label
from csbdeep.utils import normalize
import matplotlib.pyplot as plt 
from skimage import io
from csbdeep.io import save_tiff_imagej_compatible
import numpy as np

def get_arg_parser():
    parser = argparse.ArgumentParser(description='Stardist Command Line Parameters')

    parser.add_argument('Stardist')           # positional argument
    parser.add_argument('-d', '--dir')      # option that takes a directory
    parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

    return parser

def runstardist(folder_path):

    # creates a pretrained model
    model = StarDist2D.from_pretrained('2D_paper_dsb2018')  
    # model.keras_model.summary()

    # Get a list of files in the folder
    file_list = os.listdir(folder_path)

    # Segment each file in the folder
    for file_name in file_list:
        if file_name.endswith('.tif') and not os.path.isdir(file_name):
            # Path to the current file
            file_path = os.path.join(folder_path, file_name)

            img = io.imread(file_path)
            img = np.array(img)

            labels, _ = model.predict_instances(normalize(img), nms_thresh=0.35)  
            

            # save the segmentation results
            output_path = os.path.join(folder_path, f'masks/seg_{file_name}') 
            io.imsave(output_path, labels, plugin='tifffile')


def main():
    args = get_arg_parser().parse_args() 
    # Provide the path to the folder containing the images
    # folder_path = '/Users/lian/Desktop/stardist/test' 
    folder_path = args.dir

    runstardist(folder_path)

if __name__ == "__main__":
    # Call the main function
    main()