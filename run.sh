#!/bin/bash

rm -f out.ppm && python3 main.py > out.ppm && playpen/qlf.sh out.ppm