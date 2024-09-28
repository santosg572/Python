#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

file_nom = sys.argv[1]
print(file_nom)

f = open(file_nom+'.txt', "r")
files = f.readlines()

nf = len(files)
#print(nf)



"""
Created on Fri Nov 26 08:58:45 2021

@author: santosg
"""


file1 = open(file_nom+'.html',"w")


#file1.writelines(L)

t1 = '''<!DOCTYPE html>
<html lang="en">
<head>
    <title>A simple HTML document</title>
</head>
<body>
'''
file1.writelines(t1)

n = 1
for fil in files:
   fil = fil.replace('\n','')
   partes = fil.split('/')
   np = len(partes)
#   print(partes[np-1])
   t2 = str(n)+' - '+'<a href="' + fil  +'">' + partes[np-1] + '</a>'
#   print(t2)
   file1.write(t2)
   file1.write('<br>')
   file1.write('\n')
   n = n+1
#t2 = '<a href="/Users/santosg/Desktop/Libros_may1221/Wang2016_Book_AbsoluteBeginnersGuideToComput.pdf">ok</a>'

t3 = '''
</body>
</html>
'''

file1.writelines(t3)


file1.close()
