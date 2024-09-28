#/bin/bash

pat="/Users/santosg/Desktop/LIBROS_TODOS_nov1721"

files=("AAA_libros"
"BBB_libros"
"CCC_libros"
"DDD_libros"
"EEE_libros"
"FFF_libros"
"GGG_libros"
"HHH_libros"
"J-Klibros"
"LLL_libros"
"MMM_libros"
"NNN_libros"
"OOO_libros"
"PPP_libros"
"QQQ_libros"
"RRR_libros"
"SSS_libros"
"TTT_libros"
"U-Z_libros")

for file1 in "${files[@]}"
do
   echo ${pat}/${file1}
   ./saca_lista.sh ${pat} ${file1} 
   python crea_Lista_Archivos.py ${file1}
   fil=${file1}"_O"
   python creaHTML.py ${fil}
done

