import re

import subprocess

patron = re.compile('[0-9]')

file = 'Lotka-Volterra'

file_out = file+'_Tit'

fil = open(file+'.txt', 'r')
filO = open(file_out+'.txt', 'w')

datos = fil.readlines()
fil.close()

n = 1
for dd in datos:
# if 'title' in dd or 'abstrac' in dd:
 if 'title' in dd:
#  filO.write(dd)
  result = subprocess.run(["trans", "-b", ":es", dd], capture_output=True, text=True)
 # print(result.stdout)
  filO.write(str(n)+' - ' + dd)
  filO.write(str(n)+' - ' + result.stdout)
  n = n+1 
  print(n)

filO.close()
 
'''
for dd in datosL:
 p = patron.search(dd)  
 if p == None:
  datosN.append(dd)

print(datosN)
'''



