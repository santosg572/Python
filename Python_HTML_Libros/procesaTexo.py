#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:07:21 2022

@author: santosg
"""

filename = 'texto.txt'
file = open(filename, 'r')
line = file.read()
line = line.replace('\n', ' ')
line = line.lower()
line = line.replace('"', ' ')

palabras = line.split(' ')

#print(palabras)

palUnicas = set(palabras)

tem = list(palUnicas)

tem.sort()

print(tem)