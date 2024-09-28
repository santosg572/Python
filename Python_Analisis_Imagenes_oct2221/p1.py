#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 03:40:55 2021

@author: santosg
"""

from PIL import Image, ImageDraw
import numpy as np

import bib_analisis_img

ii = bib_analisis_img.LeeImg('download.jpg')

ss = ii.shape

img = np.zeros(ss)

for i in range(1,ss[0]):
    for j in range(2,ss[1]):
        imgt = ii[i-1:i+2, j-1:j+2]
        print(imgt)
        



