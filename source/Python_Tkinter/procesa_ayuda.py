file = 'scrollbar_help.txt'

fil = open(file, 'r')

datos = fil.readlines()

print(len(datos))
k = 1
i = 0
while i < len(datos)-10:
  ss = datos[i]
  if '&&&&&' in ss:
    print(str(k) + ' - ' + ss)
    k = k+1
    i = i+1
    j = i+10
    for m in range(i,j):
      ss = datos[m]
      print(ss)
    i = j+1
  i = i+1
 
