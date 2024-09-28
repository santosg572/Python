#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 06:54:06 2022

@author: santosg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
cc = """
Created on Fri Jan  7 05:05:36 2022

@author: santosg \n

Este programa saca la lista de directorios que se encuentran
 
dentro de un directorio padre, en este caso es './'

"""

import sys
import time
import funcionesLinux


def Lista(dir=''):
    global DIREC 
    res = funcionesLinux.SacaLista_Dir_Otro(dir)
    if len(res) > 0:
        for pal in res:
 #           print(pal)
            DIREC.append(pal+'/')
            Lista(pal+'/')
            
print(cc)


#time.sleep(3)

#val = input("Mete el directorio padre [./]: ")
global DIREC 

DIREC=[]

#dir1 = './'
#dir1 = '/Users/santosg/Desktop/LIBROS_TODOS_nov1721/EEE_libros/Estadistica_Libros/'
dir1 = '/Volumes/neurona/Libros_ene0722/'



#if len(val) > 0:
#    dir1 = val


Lista(dir1)

print(DIREC)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

arch = []

for pal in DIREC:
    res = funcionesLinux.SacaLista_Dir_Otro(pal,'1')
#    print(res)
    if len(res) > 0:
        for file in res: 
            arch.append(file)
        
#print(arch

res = funcionesLinux.SacaLista_Dir_Otro(dir1,'1')

for fil in res:
    print(fil)
    arch.append(fil)

funcionesLinux.CreaHTML_delista(arch, 'Estadistica_Libros.html', 'no')
