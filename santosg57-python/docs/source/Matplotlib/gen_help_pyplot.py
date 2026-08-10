file = 'help_pyplot.txt'

fil = open(file, 'r')

datos = fil.readlines()
del1 = 12

print(len(datos))

i = 0
while i < len(datos):
   if '...........' in datos[i]:
     for j in range(del1):
       ss = datos[i+j].replace('\n','')     
       print(ss)
     i = i+del1
   else:
     i = i+1


