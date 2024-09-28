#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:15:00 2021

@author: santosg
"""

import sys
import os
import subprocess 

patI = str(sys.argv[1])
folder = str(sys.argv[2])

def Buscar(patI='', folder=''):
 dir = patI+folder
 data = subprocess.Popen(['ls', '-1R', dir], stdout = subprocess.PIPE)
 res = data.communicate()
 res = str(res[0])
 res = res.replace('\\n\\n', '\\n')
 nr = len(res)
 res = res[2:(nr-3)]
 res = res.split('\\n')
 for fil in res:
  ln = len(fil)
  if fil[ln-1] == ':':
   dir = fil[:(ln-1)]
  else:
   print(dir+'/'+fil)

Buscar(patI, folder)


