#!/bin/bash

#exit 0

#for ngen in 25 50 100 500; do
for ngen in 25 50 100 500; do
    for sqln in 0 25 50 100 250; do
        # Fungi Datasets
        #for rate in 0.0 0.0000000001 0.0000000002 0.0000000005; do
        #    for size in 10000000 50000000; do
        #        modl="fungi.dlrate-$rate.psize-$size"
        #        qsub u_drive_jobs.pbs \
        #            -N "u-$modl-$sqln-$ngen" \
        #            -v arg1="$modl",arg2="$sqln",arg3="$ngen"
        #        echo "Submitted $modl $sqln $ngen"
        #    done
        #done

        # Yule Datasets
        for ntax in 25; do  #25 50 100; do
            for rate in 0.0 0.0000000001 0.0000000002 0.0000000005; do
             #for rate in 0.0000000005;do   
	    	for size in 1000 50000000; do  #1000 50000000; do
                    modl="ntaxa-$ntax.dlrate-$rate.psize-$size"
                    qsub u_drive_jobs.pbs \
                        -N "u-$modl-$sqln-$ngen" \
                        -v arg1="$modl",arg2="$sqln",arg3="$ngen"
                    echo "Submitted $modl $sqln $ngen"            
                done
            done
        done
    done
done
