#!/bin/bash

echo "Compiling C script...."
gcc fxn.c -o fxn -lm || exit 1

echo "Generating data...."
./fxn || exit 1

echo "Plotting data...."
python3 plot.py
