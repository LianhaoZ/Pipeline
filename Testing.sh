#!/bin/bash 
#SBATCH -A b1151                # Allocation
#SBATCH -p b1151                # Queue
#SBATCH -t 04:00:00             # Walltime/duration of the job - change as needed
#SBATCH --nodes=1                    # Number of Nodes
#SBATCH --mem=10G               # Memory per node in GB needed for a job. Also see --mem-per-cpu
#SBATCH --mail-user=<my_email>  # Designate email address for job communications
#SBATCH --mail-type=END     # Events options are job BEGIN, END, NONE, FAIL, REQUEUE
#SBATCH --error=<file_path>     # Path for errors must alread$
#SBATCH --job-name="test"	# Name of job

modulo purge all
conda activate /projects/b1151/lab/software/envs/cellpose 

# The purpose of this Bash Script is to run cellpose on a folder of folders each with images to segment. 
# The resulting file will be in a folder within each of the folder that the iamges are ran in.

# source /Users/lian/anaconda3/etc/profile.d/conda.sh 

# conda activate cellpose  

##### logfile #####
logfolder="log.txt" 

variable=$(grep "Done Processing folder: " "$logfolder" | sort | tail -n 1 | grep -o '[^ ]*$')
 
# default runs on gray scale channel
# change filter to "" if no filter is needed (optional)
filter="CFP" 
# change model to desired model, default is cyto2 (optional)
model="cyto2"
# change if don't estimate cell diameter (optional)
dia="0"

# provide output directory (optional)
output_dir=""

# Set folder path
folder_path="/Users/lian/Desktop/Cellpose/Num" 

# Get a list of subdirectories in the folder
subdirs=($folder_path/*/)

# time stamp
echo "$(date) - current time" >> $logfolder

#to start at folder 1
start_dir=$(find "$folder_path" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1) 

##### to start at folder other than the first folder, uncomment below #####
# start_dir=$variable 

process=false 
# Loop over each subdirectory
for dir in "${subdirs[@]}"
do 
  if [ "$dir" == "${start_dir}/" ] || [ "$dir" == "${start_dir}" ]; then
    process=true
  fi 

  if [ "$process" == true ]; then 

    echo "Processing folder: $dir" >> $logfolder

    output_folder_basename="cellpose_output"

    if [ "$output_dir" == "" ]; then
      output_dir="$dir$output_folder_basename"   
    fi
 
    if [ "$filter" == "" ]; then
      python -m cellpose --dir "$dir" --pretrained_model "${model}" --chan 0 --diameter "${dia}". --no_npy --in_folders --save_tif --savedir $output_dir
    else
      python -m cellpose --dir "$dir" --img_filter "${filter}" --pretrained_model "${model}" --chan 0 --diameter "${dia}". --no_npy --in_folders --save_tif --savedir $output_dir
    fi

      echo "Done Processing folder: $dir" >> $logfolder 
  fi
  # reset subdirectory
  output_dir=""

  # done
done

echo "Done Processing Everything" >> $logfolder 
 

# to clear the log file run below cmd
# > log.txt

conda deactivate
modulo purge all
 
# python -m cellpose --dir ~/Desktop/Cellpose/Testing1 --savedir ~/Desktop/Cellpose/Testing1 --img_filter CFP --pretrained_model cyto2 --chan 0 --diameter 0. --save_tif 
 

# chmod +x Testing.sh
# ./Testing.sh