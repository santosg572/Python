file = 'Memorias_Jornadas_2025.txt'

filin = open(file, 'r')

datos = filin.read()
datos = datos.replace('\n', ' ')

print(len(datos))

i = 0
ii = 1
del1 = 240

np1 = len(datos)
while i < np1:
  if ii < 10:
    ss = ' ' +str(ii) + '.-'
  else:
    ss = str(ii) + '.-'
#  print(ss)
  i1 = datos.find(ss, i+1)
#  print(i1)
  if i1 > 0:
    ss1 = datos[i1:(i1+del1)]
    print(ss1)
    ii = ii+1
    i = i1+del1
  else:
    i = np1


    




