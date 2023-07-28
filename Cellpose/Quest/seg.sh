#!/bin/bash 
#SBATCH -A b1151                # Allocation
#SBATCH -p b1151                # Queue
#SBATCH -t 24:00:00             # Walltime/duration of the job - change as needed
#SBATCH --nodes=1                    # Number of Nodes
#SBATCH --ntasks-per-node=1 ## how many cpus or processors do you need on each computer 
#SBATCH --mem-per-cpu=2G       # Memory per core needed for a job
#SBATCH --job-name="segnextflow"	# Name of job
#SBATCH -o /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/output/test.output    # Path for errors must alread$

modulo purge all
source activate /projects/b1151/lab/software/envs/cellpose
 
nextflow run /projects/b1151/Lian/main.nf -c /projects/b1151/Lian/nextflow.config