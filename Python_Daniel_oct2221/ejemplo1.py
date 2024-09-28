#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 03:19:29 2021

@author: santosg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("EXA_C01_S04_01.csv")

edad = datos['AGE']

i30 = sum(edad <= 39)

s1 = 0

for nn in edad:
    if nn >= 40 and nn <= 49:
        s1 = s1+1

i40 = s1


s1 = 0

for nn in edad:
    if nn >= 50 and nn <= 59:
        s1 = s1+1

i50 = s1

s1 = 0

for nn in edad:
    if nn >= 60 and nn <= 69:
        s1 = s1+1

i60 = s1

s1 = 0

for nn in edad:
    if nn >= 70 and nn <= 79:
        s1 = s1+1

i70 = s1


s1 = 0

for nn in edad:
    if nn >= 80 and nn <= 89:
        s1 = s1+1

i80 = s1

y = np.array([i30, i40, i50, i60, i70, i80])

print(y)

fac = y.cumsum()

frecrel  = np.round(y / len(edad),4)

frecrelacum = frecrel.cumsum()

print(fac)

print(frecrel)

print(frecrelacum)

h = plt.hist(edad)

alturas = h[0]
centros = h[1]
del1 = (centros[1]-centros[0])/2
centros = centros[1:11]-del1

plt.plot(centros, alturas, 'r')
plt.plot([centros[0]-2*del1, centros[0]], [0, alturas[0]])

print(h)

print(alturas)
print(centros)


plt.show()





