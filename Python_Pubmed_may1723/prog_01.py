import re

patron = re.compile('[0-9]')

file = 'Machine_Learning'
file_out = file+'_Tit_Res'

fil = open(file+'.txt', 'r')
filO = open(file_out+'.txt', 'w')

datos = fil.readlines()
fil.close()



for dd in datos:
 if 'title' in dd or 'abstrac' in dd:
  filO.write(dd)

filO.close()


'''
for dd in datosL:
 p = patron.search(dd)  
 if p == None:
  datosN.append(dd)

print(datosN)
'''



