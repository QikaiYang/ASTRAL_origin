#!/bin/bash

base="/projects/tallis/ekmolloy/multi-copy"
astrid="$base/software/ASTRID-2-nojava/ASTRID"
mappy="$base/tools/astrid_map_erin_qikai.py"

modl=$1
srep=$2
erep=$3
sqln=$4
ngen=$5

for repl in `seq -f "%02g" $srep $erep`; do
    cd $base/qikaiy2-data/$modl/$repl

    stre="astrid-raxml-sqln-$sqln-ngen-$ngen"

    do=0
    if [ ! -e $stre.tree ]; then
        do=1
    else
        empty=$(grep ";" $stre.tree)
        if [ -z $empty ]; then
            do=1
            rm $stre
        fi
    fi

    if [ $do -eq 1 ]; then
        gtre="g_trees-raxml-sqlen-$sqln-ngen-$ngen"
    	python $mappy -i $gtre.trees

        ts=$(date +%s)
        $astrid \
             -i $gtre-s2g.trees \
             -a $gtre-s2g-map.txt \
             -o $stre.tree &> $stre.log
        te=$(date +%s)
        rt=$[te - ts]

        rm $gtre-s2g.trees
        rm $gtre-s2g-map.txt
        #rm $stre.tree.1

        echo "ASTRID $modl $repl $sqln $ngen: $rt seconds"
    fi
done
