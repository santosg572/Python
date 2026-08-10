# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:28:06 2025

@author: Carlos Gil
"""


n1= 4

del1= (3 + (-1))/(n1)
area=0

x=-1
for i in range(n1+1):
  area= area + del1*(4-(x-1))**2

x= x + del1

print(area) 

