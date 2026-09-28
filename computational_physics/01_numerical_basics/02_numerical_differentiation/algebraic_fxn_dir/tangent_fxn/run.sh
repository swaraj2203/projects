#!/bin/bash

echo "Compiling C script...."

gcc tan.c -o tan -lm || exit 1

echo "Generating tangent data...."

./tan || exit 1

echo "Plotting with Python...."

python plot.py


