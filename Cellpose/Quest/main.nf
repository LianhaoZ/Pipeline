#!/usr/bin/env nextflow

nums = Channel.of( 10..99 )
/*
 * Run cellpose 
 */
process cellpose {
    input:
    val num
    
    script:
    """
    python -m cellpose --dir /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/DAPI/XY0$num --savedir /projects/b1151/Lian/Segementation_data1/20230619_expt_im012/Test --pretrained_model cyto2 --chan 0 --diameter 0. --no_npy --in_folders --save_tif  
    """
}
  
 
/*
 * Define the workflow
 */
workflow {
    cellpose(nums)  
      
}