fil = open('DataFrame.txt', 'r')

datos = fil.readlines()

i = 0
while i < len(datos):
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '&&&&&&&&&' in ss:
    i1 = i
    i2 = i+12
    for ii in range(i1, i2):
      ss = datos[ii]
      ss = ss.replace('\n', '')
      print(ss)
    i = i2
  i = i+1

