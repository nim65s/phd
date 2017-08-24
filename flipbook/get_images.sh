#!/bin/bash

FPS=5
ODDPAGES=67

rm img-*.jpg
[[ -f img1.jpg ]] || ffmpeg -i offroad.mp4 -vf fps=$FPS img%d.jpg

for ((i=1; i<=$ODDPAGES; i++ ))
do
    cp img$i.jpg img-$((2 * $i)).jpg
    cp img$(($ODDPAGES + $i)).jpg img-$(($ODDPAGES * 2 + 1 - 2 * $i)).jpg
done
