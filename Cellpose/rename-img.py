import os 
from PIL import Image
   
def renamewc(dir_path, img, channel, replace, rw): 
    new_filename = img.split('-') 

    #split up individual parts of img form .tif or other type of extension given there is only a "." separation
    for i, name in enumerate(new_filename):
        if ".tif" in name:
            new = name.split('.')
            new_filename[i] = new[0]

    #remove target channel
    contain = []
    prefix = "" 
    for i in new_filename: 
        if channel in i:
            contain.append(i)
            new_filename.remove(i) 
            
    for i in range(len(new_filename)):
        if new_filename[i] == replace:
            new_filename[i] = rw
            
    
    # If not channel name is given in image name
    if len(contain) == 0:
        print(f'WARNING: No channel name is given in image name "{img}"')
        return 

    #construct file name
    for i in new_filename:  
        prefix += i  
    
    print(new_filename)
    extension = os.path.splitext(img)[1] 
    prefix += contain[0] + extension 
    # rename
    os.rename(os.path.join(dir_path, img), os.path.join(dir_path, prefix)) 
     
def main(): 
    ################# program will rename and put anything that has "00" at the end #################
    string = "0"
    
    replace = "cp_masks_P31crop"
    rw = "mask"

    # Set the directory path
    # dir_path = "/Users/lian/Desktop/Tifs/11/masks" 
    dir_path = "/Users/lian/Desktop/Tifs/11/masks/03_RES"

    # Loop through all files in the directory
    for file_name in os.listdir(dir_path):
        # Check if the file is a TIF image
        if file_name.endswith(".tif"):
            # rename the file assuming only separation if "_" and "." 
            renamewc(dir_path, file_name, string, replace, rw)

if __name__ == "__main__":
    # Call the main function
    main()