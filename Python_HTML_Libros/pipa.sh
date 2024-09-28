#!/bin/bash

pat="/Volumes/LUPITA"

file="Libros_feb0122"

./saca_lista.sh "${pat}" "${file}"

python crea_lista_Archivos.py "${file}"

python creaHTML.py "${file}_O"
