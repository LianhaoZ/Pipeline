import os 
from PIL import Image

def rename(dir_path, img):
    channel = ["CFP", "YFP", "GFP", "TRITC", "Far-red", "DAPI"]
    new_filename = img.split('_') 

    #split up individual parts of img form .tif or other type of extension given there is only a "." separation
    for i, name in enumerate(new_filename):
        if ".tif" in name:
            new = name.split('.')
            new_filename[i] = new[0]

    #remove target channel
    contain = []
    prefix = ""
    for i in new_filename: 
        if i in channel:
            contain.append(i)
            new_filename.remove(i) 
    
    # If not channel name is given in image name
    if len(contain) == 0:
        print(f'WARNING: No channel name is given in image name "{img}"')
        return 

    #construct file name
    for i in new_filename:  
        prefix += i + "_"  
    extension = os.path.splitext(img)[1] 
    prefix += contain[0] + extension
    
    # rename
    os.rename(os.path.join(dir_path, img), os.path.join(dir_path, prefix)) 
  
            
def main():  
    # Set the directory path
    dir_path = "/Users/lian/Desktop/Cellpose/Testing1" 
    
    # Loop through all files in the directory
    for file_name in os.listdir(dir_path):
        # Check if the file is a TIF image
        if file_name.endswith(".tif"):
            # rename the file assuming only separation if "_" and "."
            rename(dir_path, file_name)

if __name__ == "__main__":
    # Call the main function
    main()