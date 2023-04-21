import os 
from PIL import Image
# import shutil

def rename(dir_path, img):  
    new_filename = img
    end = new_filename.split('_')[3]
    new_name_prefix = f"{new_filename.split('_')[0]}_{new_filename.split('_')[2]}_{end.split('.')[0]}_{new_filename.split('_')[1]}"
    extension = os.path.splitext(new_filename)[1] 
    # print(new_name_prefix)

    new_filename = f"{new_name_prefix}{extension}" 
    # print(new_filename)
    os.rename(os.path.join(dir_path, img), os.path.join(dir_path, new_filename)) 


# Set the directory path
dir_path = "/Users/lian/Desktop/Cellpose/Testing1" 
  
# Loop through all files in the directory
for file_name in os.listdir(dir_path):
    # Check if the file is a TIF image
    if file_name.endswith(".tif"):
        # rename the file 
        # new_name = os.path.join(dir_path, "copy" + file_name)
        # shutil.copyfile(os.path.join(dir_path, file_name), new_name) 
        rename(dir_path, file_name)
  