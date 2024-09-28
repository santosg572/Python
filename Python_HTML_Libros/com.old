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

#patI = '/home/soporte'
#patI = '/Users/santosg'
#dir = patI+'/Desktop/Resp_jun0622'
dir = patI+folder

data = subprocess.Popen(['ls', '-1R', dir], stdout = subprocess.PIPE)
res = data.communicate()

res = str(res[0])

res = res.split('\\n')

nr = len(res)

for i in range(1,nr-1):
    ss = res[i]
    if len(ss) > 0:
        if ss[0] == '/':
            ss= ss.replace('//','/')
            ss = ss[:len(ss)-1]
            dir = ss
        else:
            file = dir + '/' + ss
            s = os.path.isdir(file)
            if not s:
             print(file)
