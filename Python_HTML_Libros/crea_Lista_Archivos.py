#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

nombre = sys.argv[1]
nombreOUT = nombre+'_O.txt'
nombre = nombre+'.txt'

print('----------------------------------------------------------')
print('procesando el archivo= '+nombre)
print('archivo de salida' + nombreOUT)
print('----------------------------------------------------------')

f = open(nombre,"r")

lines = f.readlines()

nl = len(lines)

pat = lines[0]
pat = pat.replace('\n','')
pat = pat + '/'

print(pat)
print('pat')

fo = open(nombreOUT, "w")

for i in range(1,nl):
   cc = lines[i].replace('\n','')
   if(len(cc) > 0):
      if cc[0] == '/':
         pat = cc
         lp = len(pat)
         pat = pat[0:(lp-1)]
         pat = pat+'/'
      else:
         file = pat+cc
         print(file)
         fo.write(file)
         fo.write('\n')    


f.close()
fo.close()


