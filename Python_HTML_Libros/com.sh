#!/bin/bash

pat="/home/santosg/LIBROS_TODOS/EEE_libros/"

#../LIBROS_TODOS/PPP_libros/Python_Libros_feb0323

folder="Estadistica_Libros"

#pat="/Users/leopoldogonzalez/Desktop/LIBROS_TODOS_Toribio/RRR_libros/"
#folder="R_libros"

python3 com.py ${pat} ${folder} > ${folder}.txt

python3 creaHTML.py ${folder}

mv ${folder}.html ${pat}${folder}/.





