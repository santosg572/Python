file = 'abstract-what_is_intelligence.txt'

fil = open(file, 'r')

datos = fil.readlines()

k = 1
ln = len(datos)

i = 0
m = 3
while  i < ln:
  ss = datos[i]
  ss = ss.replace('\n', '')
  if ss[:m] == str(k)+'. ':
    print(ss)
    k = k+1
  i = i+1
    

