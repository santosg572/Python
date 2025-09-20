#!/bin/bash

pat="/mnt/datos/santosg/Libros_TODOS_antonieta/"
#"pp="AAA_libros/ DDD_libros/ GGG_libros/ J-K_libros/ NNN_libros/ Q-R_libros/"
#"BBB_libros/ EEE_libros/ HHH_libros/ LLL_libros/ OOO_libros/ SSS_libros/"
#"CCC_libros/ FFF_libros/ III_libros/ MMM_libros/ PPP_libros/ T-Z_libros/"

pat1="EEE_libros"
pat2="Estadistica_Libros"

ls -1R ${pat}${pat1}/${pat2} > ${pat2}".txt"
