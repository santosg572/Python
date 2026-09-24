file = 'help_numpy.txt'

fil = open(file, 'r')

datos = fil.readlines()

n = len(datos)
print(n)

i = 0

while i < n:
  ss = datos[i]
  ss = ss.replace('\n', '')

  if '&&&&&&' in ss:
    k = 7
    for j in range(k):
      print(datos[i+j])
    i = i+k
  i = i+1



