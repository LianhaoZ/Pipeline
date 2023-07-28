import os

# parent_directory = "/Users/lian/Desktop/stardist/" 
parent_directory = "/projects/b1151/Lian/Segementation_data1/20230619_expt_im012/DAPI/" 
 
# Iterate over the subdirectories within the parent directory
for subdir_name in os.listdir(parent_directory):
 
    subdir_path = os.path.join(parent_directory, subdir_name)

    # Check if the current item is a directory
    if os.path.isdir(subdir_path):

        # Check if the "masks" directory exists within the current subdirectory
        masks_directory = os.path.join(subdir_path, "masks")
        if os.path.isdir(masks_directory): 
            # Get the list of files in the "masks" directory
            file_list = os.listdir(masks_directory)

            # Iterate over the files and delete them
            for file_name in file_list:
                file_path = os.path.join(masks_directory, file_name)
                if os.path.isfile(file_path):
                    # os.remove(file_path)
