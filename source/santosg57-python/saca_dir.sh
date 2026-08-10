#!/bin/bash

dd=$(date +"Year: %y, Month: %m, Day: %d")
dd=$(date +"M%mD%dY%y")
echo $dd

if [ "$1" = "" ]; then
    echo
    echo "nombre del archivo"
    echo
else
    echo "bien"
    echo `pwd` > $1"_"$dd".txt"
    ls -1 `pwd` >> $1"_"$dd".txt"
fi

