#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 04:26:30 2021

@author: santosg
"""
import bib_analisis_img
import numpy as np

mat = np.arange(0,42)
mat = np.reshape(mat, (6,7))

ss = mat.shape

print(ss)

nx = ss[0]
ny = ss[1]



ii = np.random.randint(0,nx,10)

print(ii)
