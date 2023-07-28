import subprocess
import os
from cellpose import io

def run_command_on_files(folder_path): 
    for root, dirs, files in os.walk(folder_path): 
        for dir in dirs:
            file_path = os.path.join(root, dir)
            print(file_path)  
            command = f"python -m cellpose --dir {file_path} --img_filter CFP --pretrained_model cyto2 --chan 0 --diameter 0. --no_npy --in_folders --save_tif"
            subprocess.call(command, shell=True)
    
#python -m cellpose --dir /Users/lian/Desktop/Tifs/11 --pretrained_model cyto2 --chan 0 --diameter 0. --no_npy --in_folders --save_tif
 
folder_path = "/Users/lian/Desktop/Tifs"  
# folder_path = "/Users/lian/Desktop/Tracking/Sample_Tracking_Data/Trackmate7"
 

# Call the function to run the command in the folder
run_command_on_files(folder_path)
