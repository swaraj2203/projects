#!/bin/bash

echo "Compling C code...."
gcc kelper.c -o kepler -lm

echo "Running calculation...."
./kepler

echo "Generating plot...."
python3 plt.py

echo "Done!"
