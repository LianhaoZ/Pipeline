#!/bin/bash 
#SBATCH -J Stardist             	# Name of job
#SBATCH -A b1151                # Allocation
#SBATCH -p b1151                # Queue
#SBATCH --nodes=1
#SBATCH --ntasks=5
#SBATCH -t 24:00:00             # Walltime/duration of the job - change as needed 
#SBATCH --cpus-per-task=1   # Number of cores (= processors = cpus) for each$
#SBATCH --mem-per-cpu=2G       # Memory per core needed for a job
#SBATCH --array=1-9            # number of parallel jobs to run counting from 0. Make sure to change this to match total number of files.
#SBATCH -o /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/output/test.output    # Path for errors must alread$

echo "Hello ${SLURM_ARRAY_TASK_ID}"