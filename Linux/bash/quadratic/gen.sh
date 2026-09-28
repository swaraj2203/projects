#!/bin/bash

xmin=$1
xmax=$2

> quadratic.dat

for x in $(seq $xmin $xmax)
do
	y=$((x * x))
	echo "$x $y" >> quadratic.dat
done

python3 plot.py

