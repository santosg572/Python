file = "help_matplotlib.txt"

fil = open(file, 'r')

datos = fil.readlines()

n = len(datos)
i = 0

while i < n:
  ss = datos[i]
  ss = ss.replace('\n','')
  if '&&&&&&&&' in ss:
    k = 7
    for j in range(k):
      ss = ss = datos[i+j]
      ss = ss.replace('\n','')
      print(ss)
    i = i+k
  i = i+1



