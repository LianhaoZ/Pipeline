#!/bin/bash 
#SBATCH -A b1151                 
#SBATCH -p b1151               
#SBATCH -t 24:00:00              
#SBATCH --nodes=1                     
#SBATCH --cpus-per-task=1    
#SBATCH --mem-per-cpu=2G        
#SBATCH --job-name="hello"     

modulo purge all
source activate /projects/b1151/lab/software/envs/cellpose
 
nextflow run /projects/b1151/Lian/hello.nf -c /projects/b1151/Lian/nextflow.config