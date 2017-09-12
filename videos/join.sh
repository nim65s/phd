#!/bin/bash

ffmpeg -i lemurdanslemiroir.mp4 -i palkeo.mp4 \
    -filter_complex '[0:v]pad=2038:720[int];[int][1:v]overlay=1280:0[vid]' \
    -map [vid] -c:v libx264 -an offroad.mp4
