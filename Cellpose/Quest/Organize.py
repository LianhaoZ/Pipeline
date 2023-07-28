import os
import shutil

def organize_folders(source_dir):
    categories = ["DAPI", "GFP"]

    for file in os.listdir(source_dir):
        if file.endswith(".tif"):
            pos_xy = file.split("_")[2]  # Extracting XY position from the file name

            for category in categories:
                if category in file:
                    category_folder = os.path.join(source_dir, category)
                    os.makedirs(category_folder, exist_ok=True)

                    pos_folder = os.path.join(category_folder, pos_xy)
                    os.makedirs(pos_folder, exist_ok=True)

                    source_file = os.path.join(source_dir, file)
                    destination_file = os.path.join(pos_folder, file)
                    shutil.move(source_file, destination_file)
                    break
 
if __name__ == "__main__":
    source_directory = "/Volumes/microscope/scope1/datadrive_F/users/KL/2023/20230619_expt_im012/tifs"  # Path to the source directory

    organize_folders(source_directory)
