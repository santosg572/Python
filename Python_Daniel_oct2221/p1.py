#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 02:34:01 2021

@author: santosg
"""

import matplotlib.pyplot as plt
import bib_daniel

# 'GenDisNormal_XY', 'GenFrecuenciaAcum', 'GrafPoligonoFrecuencias',

print(help(bib_daniel.GrafPoligonoFrecuencias))


res = bib_daniel.GrafPoligonoFrecuencias([1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7], 8)

#plt.plot(res[0], res[1])

#plt.show()

