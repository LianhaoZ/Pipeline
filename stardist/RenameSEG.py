import os

folder_path = '/Users/lian/Desktop/stardist/Scoring_SEG/01_RES'
file_extension = '.tif'
new_prefix = 'mask'

# Get a list of all files in the folder with the specified extension
files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]

# Rename each file
for old_filename in files:
    file_path = os.path.join(folder_path, old_filename)
    suffix = old_filename.split("_")[3]
    s = suffix.split("XY")[1]
    new_filename = new_prefix + s + ".tif"
    new_file_path = os.path.join(folder_path, new_filename)
    os.rename(file_path, new_file_path)
    print(f"File '{old_filename}' has been renamed to '{new_file_path}'.")

print("All files have been renamed.")
