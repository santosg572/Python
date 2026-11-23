file = 'sns_funciones_help.txt'

fil = open(file, 'r')

datos = fil.readlines()

ln = len(datos)

i=0
while i < ln:
  ss = datos[i]
  ss = ss.replace('\n', '')
  if '%%%%%' in ss:
    dd = ss.split(' ')
    file1 = dd[1]+'.rst'
    fil1 = open(file1,'w')
    i = i+1
    while i < ln:
      ss = datos[i]
      ss = ss.replace('\n', '')
      if '%%%%%' in ss:
        fil1.close()
        break
      else:
        fil1.write(ss+'\n')
        i = i+1
  i = i+1
