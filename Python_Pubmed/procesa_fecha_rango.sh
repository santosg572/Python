#!/bin/bash

mes=10

dia=02
 
yy=24

filo="fecha_rango_M"${mes}"D"${dia}"y"${yy}
echo $filo

python fecha_rango.py $mes $dia $yy > ${filo}".txt"

filt=${filo}"_titulos" 
cat ${filo}".txt" | grep \"title\": > ${filt}".txt" 




