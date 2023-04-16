#!/bin/bash

rdir=/scratch/klb327/pi/pimeta/results
numfiles=`ls $rdir | wc -l` 
cd $rdir

header="pi_length;shortest_answer;num_answers;answers"
echo $header

for x in `seq $numfiles` 
do
	sed -i 's/[][ ]//g' $x.txt
	count=`cat $x.txt | awk -F ',' '{print NF}'`
	length=`cat $x.txt | awk -F ',' '{print $1}' | wc -c`
	answers=`cat $x.txt`
	echo "$x;$length;$count;$answers" 	
	
	
	
done
