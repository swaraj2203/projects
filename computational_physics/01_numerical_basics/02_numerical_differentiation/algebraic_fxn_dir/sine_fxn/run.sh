#!/bin/bash

echo "Compiling C script...."

gcc sine_curve.c -o sine_curve -lm || exit 1

echo "Compliation complete...."

echo "Executing C script...."

./sine_curve || exit 1

echo "C scripted executed sucessfully!"

echo "Plotting results on Python...."

python3 plot.py


