
filin = open('numpy_help.txt', 'r')

datos = filin.readlines()

print(len(datos))

i = 0

del1 = 10

while (i < len(datos)):
  if '================' in datos[i]:
    ss1 = datos[i].replace('\n','')
    ss1 = ss1.replace('=','.')
    print(ss1)
    i = i+1
    for j in range(del1):
      ss = datos[i+j].replace('\n','')
      print(ss)
    i = i + del1
  else:
    i = i+1

  
