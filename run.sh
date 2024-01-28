#!/bin/bash

rm -f out.ppm && time (python3 main.py > out.ppm) && playpen/qlf.sh out.ppm