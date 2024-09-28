#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:37:14 2021

@author: santosg
"""
import numpy as np
import pandas as pd

def Simetria(x = 0):
    # supongo que x es un arreglo numpy
    n = len(x)
    xm = np.mean(x)
    
    num = np.sqrt(n) * sum((x-xm)**3)
    
    den = (sum((x-xm)**2))**(3/2)
    return num/den

def Kurtosis(x = 0):
    # supongo que x es un arreglo numpy
    n = len(x)
    xm = np.mean(x)
    
    num = n * sum((x-xm)**4)
    
    den = (sum((x-xm)**2))**2
    return num/den - 3
    
