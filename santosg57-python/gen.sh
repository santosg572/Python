#!/bin/bash

dir="santosg57-python"

./saca_dir.sh $dir

file=$(ls -1 $dir*.txt)

echo $file

filen=${file%.*}

echo $filen

python creaHTML.py  $filen




