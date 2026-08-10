file = 'help_matplotlib_pyplot.txt'

fil = open(file, 'r')

datos = fil.readlines()
fil.close()

i = 0
nl = 15

while i < len(datos)-nl:
  ss = datos[i]
  if '&&&&&&&&&&&&&&&&&&&&&' in ss:
    for j in range(i, i+nl):
      print(datos[j])
    i = i+nl     
  else:
    i = i+1
 
