# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 20:29:27 2025

@author: Carlos Gil
"""

import math

print('\n\nParámetros de la medición de longitud de pie\n\n')

x=[36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 40, 36, 42, 43,  41, 42, 39,
   36, 36, 43, 41, 36, 45, 38, 40, 37.5]


np1= len(x)

def media(li=[]):
    nl = len(li)
    sum = 0
    
    for x in li:
        sum = sum + x
    return sum/nl

def varianza(li=[]):
    nl= len(li)
    xm = media(li)
    
    sum = 0
    for x in li:
        sum = sum + (x-xm)**2
    return sum/(nl-1)
    
    for x in li:
        sum = sum 
def desvest(li=[]):
    n1= len(li)
    xv = varianza(li)
    
    sum = 0
    for x in li:
        sum = sum + (math.sqrt(xv))
    return sum/(n1-1)    

def tercera(li=[]):
    n1= len(li)
    xt= media(li)

    sum = 0
    for x in li:
        sum = sum + (x-xt)**3
    return sum/(n1)

def asimetria(li=[]):
    n1= len(li)
    xk= tercera(li)

    sum = 0
    for x in li:
        sum = sum + (xk/(2.966486107676365)**3)
    return sum/(n1)

print('La media de x es', media([36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 40, 36, 42, 
   43,  41, 42, 39, 36, 36, 43, 41, 36, 45, 38, 40, 37.5]))

print('La varianza de x es', varianza([36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 
      40, 36, 42, 43,  41, 42, 39, 36, 36, 43, 41, 36, 45, 38, 40, 37.5]))

print('La desviación estándar de x es', desvest([36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 
      40, 36, 42, 43,  41, 42, 39, 36, 36, 43, 41, 36, 45, 38, 40, 37.5]))

print('La diferencia a la tercera potencia de x es', tercera([36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 
      40, 36, 42, 43,  41, 42, 39, 36, 36, 43, 41, 36, 45, 38, 40, 37.5]))

print('Asimetria de x es', asimetria([36, 39, 35, 37, 36, 38, 39, 43, 41, 36, 36, 
      40, 36, 42, 43,  41, 42, 39, 36, 36, 43, 41, 36, 45, 38, 40, 37.5]))
