# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:17:07 2025

@author: Carlos Gil
"""

import math

x= [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00]
y= [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]

np1= len(x)

sum_y = 0

for i in range(np1):
  sum_y= sum_y+ x[1]+y[1]
   
print('La sumatoria de y es', sum_y)

media = (sum_y/(i-1))
print('La media de y es', media)

sum_xy= sum(xi*yi for xi, yi in zip(x, y))

print ('La suma de la multiplicacion de xy es', sum_xy)

sum_x= sum(x)
print('La sumatoria de x es', sum_x)

avg = (sum_x/(i-1))
print('La media de x es', avg)

t1= (sum_xy-(10*(media*avg)))

print('El numerador es', t1)

sq = (sum_x)**2
print('La sumatoria de x al cuadrado es', sq)

sqnum= sq/10
print('La sumatoria de x al cuadrado es', sqnum)


def sum_cuad_for(x):
    suma=0
    for x in x:
        suma += x**2
    return suma
print('La sumatoria de cuadrados de x es', sum_cuad_for(x))

t2 = ((sum_cuad_for(x))-sqnum)  
print('El denominador es',t2)

#para total
total=(t1/t2)

print('La pendiente es', total)

intercepto= (media-(avg+total))

print('El intercepto es', intercepto)