#!/bin/bash

for video in *.mp4
do
    ffmpeg -y -i $video -vframes 1 -f image2 $video.jpg
done
