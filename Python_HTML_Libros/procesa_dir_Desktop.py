filename = 'dir_Desktop_abr06_CASA.txt'

file = open(filename, 'r')
datos = file.readlines()

file.close()

print(type(datos))

nl = len(datos)

pat = './'

print(nl)
print(datos[0])

for i in range(nl):
 reg = datos[i]
 reg = reg.replace('\n', '')
 reg = reg.replace(':', '')
 if  len(reg) > 1:
#  print(reg[0])
  if reg[0] == '/':
   print('\n')
   pat = reg
  else:
   file = pat+'/'+reg 
   ll = len(file)
   ss = file[ll-4:ll]
 #  print(ss)
   if ss == '.pdf' or ss == '.PDF':
    print(file)



