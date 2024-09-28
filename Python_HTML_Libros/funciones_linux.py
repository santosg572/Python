#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:42:58 2021

@author: santosg
"""

import subprocess 

def SacaDir():
    dir = '/Users/santosg/Desktop/Libros_may1221/' 
    data = subprocess.Popen(['ls', '-1R', dir], stdout = subprocess.PIPE) 
    res = data.communicate() 
    res = str(res[0]) 
    res = res.split('\\n') 
    
    direc = []
    for ss in res: 
        if len(ss) > 0: 
            if ss[0] == '/': 
                ss= ss.replace('//','/') 
                ss = ss[:len(ss)-1] 
                dir = ss 
            else: 
                file = dir + '/' + ss
                direc.append(file)
    
    return direc
