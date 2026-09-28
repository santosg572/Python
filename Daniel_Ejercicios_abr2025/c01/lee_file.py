file = 'EXA_C01_S04_01.csv'

fil = open(file, 'r')

datos = fil.readlines()

datos = datos[1:]

dd = list()

for ss in datos:
  ss = ss.replace('\n', '')
  ss1 = ss.split(',')
  x = int(ss1[1])
  dd.append(x)

print(dd)



