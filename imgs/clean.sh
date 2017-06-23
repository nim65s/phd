#!/bin/bash


for img in *.jpg *.png
do
    convert $img -fuzz 1% -trim +repage trim.${img##*.}
    mv trim.${img##*.} $img
done

jpegoptim -s *.jpg
optipng -o2 *.png
