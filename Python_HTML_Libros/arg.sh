#!/bin/bash

pat="/Users/santosg/Desktop/ Resp_jun0622"
folder="Resp_jun0622"
python com.py $pat $folder > ${folder}.txt

python creaHTML.py ${folder}





