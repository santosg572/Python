file = 'matplotlib_funciones'

fil = open(file+'.txt', 'r')

datos = fil.readlines()

fileN = file + '_resumido.txt'

filN = open(fileN, 'w')

nl = len(datos)

i = 0
while i < nl:
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '&&&&&&' in ss:
    i1 = i
    i2 = i + 12
    if i2 >= nl:
      i2 = nl

    for j in range(i1, i2):
      ss = datos[j]
      ss = ss.replace('\n', '')
      filN.write(ss+'\n')
    
    i = i2

  i = i+1
