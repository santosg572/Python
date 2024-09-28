#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:36:01 2022

@author: santosg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:07:21 2022

@author: santosg
"""

filename = 'texto.txt'
file = open(filename, 'r')
line = file.read()
line = line.replace('\n', ' ')
line = line.replace('.', ',')
line = line.replace('?', ',')

line = line.lower()


oraciones = line.split(', ')

fic = open("temporal.txt", "w")

nn = 1
for ora in oraciones:
    print(ora)
    fic.write(str(nn)+' - ' +ora)
    fic.write("\n")
    nn = nn+1
    
fic.close()