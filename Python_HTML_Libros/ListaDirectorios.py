#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 06:53:19 2022

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

#print(cc)
#time.sleep(3)

#val = input("Mete el directorio padre [./]: ")

dir1 = './'
#dir1 = '/Users/santosg/Desktop/LIBROS_TODOS_nov1721/'
#dir1 = '/Users/santosg/Desktop/LIBROS_TODOS_nov1721/EEE_libros/Estadistica_Libros/'

#f len(val) > 0:
#    dir1 = val+'/'


res = funcionesLinux.SacaLista_Dir_Otro(dir1, 0)

if len(res) > 0:
    print(res)
else:
    print('NO HUBO Directorios')