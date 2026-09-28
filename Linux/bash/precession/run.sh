#!/bin/bash

set -e

echo "Compiling C code...."
gcc precession.c -o precession -lm

echo "Running orbital simulation...."
./precession

echo "Creating animation...."
python3 animate.py

echo "Done!"

