#!/bin/bash

FPS=5
ODDPAGES=54

rm *.jpg
ffmpeg -i offroad.mp4 -vf fps=$FPS img%d.jpg

for ((i=1; i<=$ODDPAGES; i++ ))
do
    mv img$i.jpg img-$((2 * $i)).jpg
    mv img$(($ODDPAGES + $i)).jpg img-$(($ODDPAGES * 2 + 1 - 2 * $i)).jpg
done
