#!/bin/bash


for img in *.jpg *.png
do
    convert -flatten $img -fuzz 1% -trim +repage $img
done

jpegoptim -s *.jpg
optipng -strip all -nx -o2 *.png
