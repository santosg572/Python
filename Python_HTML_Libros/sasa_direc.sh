#!/bin/bash

dd=`ls -1R $1`

for file1 in $dd
do
   size=${#file1}
   if [ $size -gt 0 ]
   then
      echo ${file1}
      echo $size
   fi
done





