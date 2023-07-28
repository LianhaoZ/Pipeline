#!/bin/bash 
#SBATCH -A b1151                # Allocation
#SBATCH -p b1151                # Queue
#SBATCH -t 08:00:00             # Walltime/duration of the job - change as needed
#SBATCH --nodes=1                    # Number of Nodes
#SBATCH --mem=10G               # Memory per node in GB needed for a job. Also see --mem-per-cpu
#SBATCH --mail-user=<my_email>  # Designate email address for job communications
#SBATCH --mail-type=END     # Events options are job BEGIN, END, NONE, FAIL, REQUEUE
#SBATCH --error=<file_path>     # Path for errors must alread$
#SBATCH --job-name="cellpose"	# Name of job

modulo purge all
source activate /projects/b1151/lab/software/envs/cellpose
 
nextflow run /projects/b1151/Lian/main.nf -C /projects/b1151/Lian/nextflow.config
 
Input= /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/DAPI/XY$SLURM_ARRAY_TASK_ID
Output = `echo $Input `
 