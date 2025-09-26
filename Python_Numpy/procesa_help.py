file= 'help.txt'

filin = open(file, 'r')
datos = filin.readlines()
filin.close()
nr = 12

i = 0
while (i < len(datos)):
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '&&&&&&&&&&&&&&' in ss:
    for j in range(i, i+nr):
      ss1 = datos[j]
      ss1 = ss1.replace('\n', '')
      print(ss1)
    i = i+nr
  else:
    i = i+1

    
