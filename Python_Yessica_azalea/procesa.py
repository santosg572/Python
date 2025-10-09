file = 'img_help.txt'

fil = open(file, 'r')

datos = fil.readlines()

i=0
while i < len(datos):
  ss = datos[i]
  ss = ss.replace('\n','')
  if '&&&&&&&&&&&&&' in ss:
    i1 = i
    i2 = i+15
    for ii in range(i1, i2):
      s1 = datos[ii]
      s1 = s1.replace('\n','')  
      print(s1)
    i = i2+1
  else:
    i = i+1

