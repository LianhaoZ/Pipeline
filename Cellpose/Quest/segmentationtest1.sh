#!/bin/bash 
#SBATCH -J cellpose             	# Name of job
#SBATCH -A b1151                # Allocation
#SBATCH -p b1151                # Queue
#SBATCH --nodes=1
#SBATCH --ntasks=5
#SBATCH -t 24:00:00             # Walltime/duration of the job - change as needed 
#SBATCH --cpus-per-task=1   # Number of cores (= processors = cpus) for each$
#SBATCH --mem-per-cpu=2G       # Memory per core needed for a job
#SBATCH --array=100-119            # number of parallel jobs to run counting from 0. Make sure to change this to match total number of files.
#SBATCH -o /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/output/test.output    # Path for errors must alread$

module purge all
source activate /projects/b1151/lab/software/envs/cellpose

python -m cellpose --dir /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/DAPI/XY$SLURM_ARRAY_TASK_ID --pretrained_model cyto2 --chan 0 --diameter 0. --no_npy --in_folders --save_tif  

 