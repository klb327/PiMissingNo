#!/bin/bash

# run sspi.py for various lengths of pi

piinput=/scratch/klb327/pi/pi500m.txt 
sspipath=/home/klb327/sspi/sspi.py
wdir=/scratch/klb327/pi/pimeta/ 
rdir=/scratch/klb327/pi/pimeta/results
cd $wdir

#check all lengths of pi from 1 to this variable 
metasearchspace=1000


for x in `seq 10000`
do
	head -c $x $piinput > pi$x.txt
	python $sspipath -f pi$x.txt -j > $rdir/$x.txt 
done 
