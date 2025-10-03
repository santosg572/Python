#!/bin/bash

file=$1

cat ${file}".txt" | grep '"title":' > ${file}"_title.txt"



