import os
import numpy as np
from skimage import io
from cellpose import metrics
import shutil 
 


def IOU(cellpose_folder, ground_truth_folder, output):

    # Get the list of files in both folders
    cellpose_files = sorted(os.listdir(cellpose_folder))
    ground_truth_files = sorted(os.listdir(ground_truth_folder))

    iou_scores = []
    cellpose_f = []

    # Iterate over each file pair
    for cellpose_file, ground_truth_file in zip(cellpose_files, ground_truth_files):
        # Load Cellpose segmented mask

        # Check if both files end with ".tif"
        if cellpose_file.endswith(".tif") and ground_truth_file.endswith(".tif"):
            
            print(cellpose_file)
            print(ground_truth_file)

            cellpose_mask = io.imread(os.path.join(cellpose_folder, cellpose_file))
            
            # Load ground truth image
            ground_truth_image = io.imread(os.path.join(ground_truth_folder, ground_truth_file))

            # Testing1: when given image is different than ground truth by a pixel, index should go down --> checked (given 2 images are the same thus previously index == 1) #
            image_array = np.array(cellpose_mask, dtype=np.float32)
            image_width = image_array.shape[1]

            # # Switch half of the pixels to 255
            # if image_width % 1024 == 0:
            #     half_width = image_width // 1024
            #     image_array[:, :half_width] = 255 
            # # image_array[:] = 255

            # Convert the modified image array back to an image
            ground_truth_image = np.asarray(image_array, dtype=np.uint8) 
            # //////// end of test1 #
            
            # Calculate IOU score
            iou_score = metrics.aggregated_jaccard_index(cellpose_mask, ground_truth_image)
        
        
            mean_iou = np.nanmean(iou_score)  

            has_nan = np.isnan(image_array) # There is Nan values in the NP array
            if has_nan.any():
                print("error100")
        
            # Print individual IOU score 
            print(f"IOU Score for {cellpose_file}: {mean_iou}") 
        
            # iou_scores.append(mean_iou)
            # cellpose_f.append(cellpose_file)


    # # Calculate mean IOU score 
    # print(f"Mean IOU Score: {iou_scores}") 

    # # Concatenate the IOU array and the Cellpose files as columns
    # data = np.column_stack((cellpose_f, iou_scores))

    # # Create a header row
    # header = 'Cellpose Files,IOU'

    # # Specify the directory and filename
    # outputpath = output
    
    # np.savetxt(outputpath, data, delimiter=',', header=header, comments='', fmt='%s')

def main(): 
    cellpose_folder = "/Users/lian/Desktop/Cellpose/Num/11/cellpose_output/masks"
    ground_truth_folder = "/Users/lian/Desktop/Cellpose/Num/11/cellpose_output/masks"

    output = '/Users/lian/Desktop/Cellpose/Num/iou_labels.csv'

    IOU(cellpose_folder, ground_truth_folder, output)

if __name__ == '__main__':
    main()