#!/bin/bash 

source /Users/lian/anaconda3/etc/profile.d/conda.sh

conda activate cellpose 

# default runs on gray scale channel
# change filter to "" if no filter is needed
filter="CFP" 
# change model to desired model, default is cyto2
model="cyto2"
# change if don't estimate cell diameter
dia="0"

# provide output directory
output_dir=""

# Set folder path
folder_path="/Users/lian/Desktop/Cellpose/Num" 

# Get a list of subdirectories in the folder
subdirs=($folder_path/*/)

# Loop over each subdirectory
for dir in "${subdirs[@]}"
do
  echo "Processing folder: $dir"

  output_folder_basename="cellpose_output"

  if [ "$output_dir" == "" ]; then
    output_dir="$dir$output_folder_basename"  
    echo $output_dir
  fi
  # # Loop over each .tif file in the subdirectory
  # for file in $(ls -v "$dir"*.tif)
  # do 
    # echo "Processing file: $file" 
  if [ "$filter" == "" ]; then
    python -m cellpose --dir "$dir" --pretrained_model "${model}" --chan 0 --diameter "${dia}". --no_npy --in_folders --save_tif --savedir $output_dir
  else
    python -m cellpose --dir "$dir" --img_filter "${filter}" --pretrained_model "${model}" --chan 0 --diameter "${dia}". --no_npy --in_folders --save_tif --savedir $output_dir
  fi
    echo "Done Processing file: $file"   
  # done
  output_dir=""
done

 
 
# python -m cellpose --dir ~/Desktop/Cellpose/Testing1 --savedir ~/Desktop/Cellpose/Testing1 --img_filter CFP --pretrained_model cyto2 --chan 0 --diameter 0. --save_tif 
 

# chmod +x Testing.sh
# ./Testing.sh