#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 04:53:45 2021

@author: santosg
"""

import pandas as pd
import numpy as np
from scipy import stats

import bib_daniel

datos = pd.read_csv("EXA_C01_S04_01.csv")

edad = datos['AGE']

#bib_daniel.GrafPoligonoFrecuencias(edad, 5)


#tati = bib_daniel.Gen_TablaFrecuencias(edad, 6)

#print(tati)

np.sort(edad)

print(stats.describe(edad))
