#!/usr/bin/env nextflow

nums = Channel.of( 10..11 )
/*
 * Run cellpose 
 */
process hello {
    input:
    val num
    
    output: 
    stdout

    script:
    """
    echo hello $num
    """
}
  
 
/*
 * Define the workflow
 */
workflow {
    hello(nums) 
}