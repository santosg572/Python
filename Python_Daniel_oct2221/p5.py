#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:10:19 2021

@author: santosg
"""

import pandas as pd

datos = pd.read_csv('datos.csv')

print(type(datos))

nombre = datos['sexo':'f','nombre']

print(type(nombre))

print(nombre)