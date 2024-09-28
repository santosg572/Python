#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 04:58:03 2022

@author: santosg
"""

import funcionesLinux  as fun 

dir = '/Users/santosg/Desktop/'
#dir = './'
dir = './dd/'
dir = '../Desktop/LIBROS_TODOS_nov1721/EEE_libros/Estadistica_Libros'
dir = '/Volumes/neurona/Libros_ene0722/'

lista = fun.SacaLista_Dir_Otro(dir,'1') 

for fil in lista:
    print(fil)