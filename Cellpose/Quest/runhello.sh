#!/bin/bash 
#SBATCH -J cellpose             	## Name of job
#SBATCH -A b1151                ## Allocation
#SBATCH -p b1151                ## Queue
#SBATCH -t 24:00:00             ## Walltime/duration of the job - change as needed
#SBATCH --nodes=1 ## how many computers do you need
#SBATCH --ntasks-per-node=1 ## how many cpus or processors do you need on each computer 
#SBATCH --mem-per-cpu=2G       ## Memory per core needed for a job
#SBATCH --array=0-3
#SBATCH -o /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/output/test.output    ## Path for errors must alread$

echo "hello" >> "/projects/b1151/Lian/Segementation_data1/20230619_expt_im012/output/test.output"