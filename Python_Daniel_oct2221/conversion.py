#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:03:23 2021

@author: santosg
"""

import matplotlib.pyplot as plt

import numpy as np


a = np.array([4,2,5,3])

b = [4,3,2,5]

c = np.resize(list(range(12)), (3,4))


w = [a,b,c]

print(w)

plt.plot(w[2][1,], w[2][2,])

plt.show()






