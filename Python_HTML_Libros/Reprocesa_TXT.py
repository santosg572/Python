file = "Estadistica_Libros.txt"

fil = open(file, 'r')
datos = fil.readlines()

pat='/'
for ss in datos:
  ss = ss.replace('\n','')
  if len(ss) > 0:
    print(ss)
    if ss[0] == '/':
      np1 = len(ss)
      pat = ss[:np1]
      print('dir'+pat)
    else:
      dd = pat+'/'+ss
      print(dd)

      

