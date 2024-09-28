#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:19:27 2021

@author: santosg
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def GenDisNormal_XY(mu=0, sd=0):
    '''
    Genera la Función de Densidad de la  Distribución Normal con media=mu y desciación 
    estándar=sd

    Parameters
    ----------
    mu : TYPE float
        DESCRIPTION. The default is 0.
    sd : TYPE, float
        DESCRIPTION. The default is 0.

    Returns
    -------
    z : TYPE lista: 1er elemento, valores de x
                    2o elemento, valores de densidad

    '''
    
    x = np.arange(mu-4*sd, mu+4*sd,.1)
    ss = (x-mu)**2 / (2*sd**2)
    fi = np.exp(-ss) / (sd * np.sqrt(2 * np.pi))
    
    z = [x, fi]
    
    return z

def GenFrecuenciaAcum(mu=0, sd=0):
    '''
    Genera la frecuencia acumulada de una distribución
    normal con media=mu y desviación estandar=sd

    Parameters
    ----------
    mu : TYPE, float
        DESCRIPTION. The default is 0.
    sd : TYPE, float
        DESCRIPTION. The default is 0.

    Returns
    -------
    list
        regres una lista:
            1er elemento, valores de x
            2o  elemento, valores de la frcuencia acumulada
            
    '''
    y = GenDisNormal_XY(mu, sd)
    x = y[0]
    fi = y[1] 
    fiacum = np.cumsum(fi)
    return [x, fiacum]


def GrafPoligonoFrecuencias(x = 0, nbi=0):
    '''
    Grafica el poligono de frecuencias de un vector

    Parameters
    ----------
    x : TYPE, array
        DESCRIPTION. The default is 0.
    nbin : TYPE, entero positivo, numero de bins del histograma
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    '''
    
    tt = plt.hist(x, nbi)
    
    print(tt)
    
    fre = tt[0]
    print(type(fre))
    x = tt[1]
    nx = len(x)
    x = x[:(nx-1)]
    print(x)
    
    del1 = (x[1] - x[0])/2
    
    x = x+del1
    
    x = np.append(x[0]-2*del1, x)
    x = np.append(x, x[nx-1]+2*del1)
    fre = np.append(0, fre)
    fre = np.append(fre, 0)
    
    print(x)
    print(fre)
 #   print(fre)

    plt.plot(x,fre, 'r')
    

def Gen_TablaFrecuencias(x=0, nbi=0):
    tt = plt.hist(x, nbi) 
    
    
    fre = tt[0]
    
    x = tt[1]
    nx = len(x)
    x = x[:(nx-1)]
    
    frecacum = np.cumsum(fre)
    frecRel = fre/sum(fre)
    frecRelAcum = frecacum / sum(fre)
    
    tabla = pd.DataFrame({'frec': fre, 'frecacum':frecacum, 'frecRel':frecRel, 'frecRelAcum':frecRelAcum})
    
    
    return tabla
    
    
    
    
    

    