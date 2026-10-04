#file = 'dir_pandas_help.txt'

file = 'help_pandas_DataFrame.txt'

fil = open(file, 'r')

datos = fil.readlines()

n = len(datos)

i = 0
while i < n:
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '&&&&&&' in ss:
    i1 = i
    i2 = i + 11
    for j in range(i1, i2):
      ss = datos[j]
      ss = ss.replace('\n', '')
      print(ss)
    i = i2
  i = i+1

