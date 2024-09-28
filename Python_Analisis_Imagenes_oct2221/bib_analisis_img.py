#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 03:37:21 2021

@author: santosg
"""

#http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#functions

from PIL import Image, ImageDraw
import numpy as np


def LeeImg(nombre=''):
    jpgfile = Image.open(nombre) 
    print(dir(jpgfile)) 
    print(jpgfile.bits, jpgfile.size, jpgfile.format) 
    image = np.array(jpgfile)
    print(image.shape) 
    img = image[:,:,1] 
    print(img.shape) 
    return np.uint8(img)

def InvertImg(ii=0):
    x2 = np.max(ii)
    x1 = np.min(ii)

    img = x2 + x1 - ii
    
    return img


def FiltroMedio(mat=0):
    ss = mat.shape

    print(mat)

    for i in range(1,ss[0]-1):
        for j in range(1,ss[1]-1): 
            matt = mat[i-1:i+2, j-1:j+2]
            me = round(np.mean(matt))
            print(me)

