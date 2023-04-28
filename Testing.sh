#!/bin/bash

# Print a greeting message
echo "Hello, World!"

# Print the current date and time
# date

# chmod +x Testing.sh
# ./Testing.sh
base_dir= "/Users/lian/Desktop/Cellpose/Num" 

for subfolder in "${base_dir}"/*; 
do
  echo "Processing folder: $subfolder"
  for file in $subfolder/*.tif
  do
    echo "Processing file: $file" 
    python -m cellpose --dir $folder --img_filter CFP --pretrained_model cyto2 --chan 0 --diameter 0. --save_tif 
    echo "Done Processing file: $file" 
  done
done



# python -m cellpose --dir ~/Desktop/Cellpose/Testing1 --savedir ~/Desktop/Cellpose/Testing1 --img_filter CFP --pretrained_model cyto2 --chan 0 --diameter 0. --save_tif 