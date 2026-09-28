#!/bin/bash

echo "Compiling C code...."
gcc curve.c -o curve -lm

echo "Generating data...."
./curve

echo "Creating animation...."
python3 animate.py

echo "Finished...."

