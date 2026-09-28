#!/bin/bash

echo "Compiling C script...."
gcc limit.c -o limit -lm || exit 1

echo "Generating data...."
./limit || exit 1

echo "Plotting error...."
python3 plot.py
