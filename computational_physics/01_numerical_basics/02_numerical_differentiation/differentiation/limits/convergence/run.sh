#!/bin/bash

echo "Compiling C script...."
gcc diff.c -o diff -lm || exit 1

./diff || exit 1
echo "Generating data...."

echo "Plotting data...."
python3 plot.py
