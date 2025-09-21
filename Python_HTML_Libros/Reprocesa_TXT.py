file = "Estadistica_Libros.txt"

dd1= '''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
'''
#<h1>This is a Heading</h1>
#<p>This is a paragraph.</p>

dd2='''
</body>
</html> 
'''


fil = open(file, 'r')
datos = fil.readlines()
fil.close()

filo = open('dd.html', 'w')
filo.write(dd1)

pat='/'

k = 1
for ss in datos:
  ss = ss.replace('\n','')
  if len(ss) > 0:
#    print(ss)
    if ss[0] == '/':
      np1 = len(ss)
      pat = ss[:(np1-1)]
#      print('dir'+pat)
    else:
      dd = pat+'/'+ss
      print(dd)
#      ddx = '<p> <a href="https://' +dd[1:] + '">¡Visita Semrush!</a> </p>\n'
      ddx = '<p> <a href="' +dd + '"> Libro-'+ str(k) +'</a> </p>\n'
      ddy = '<object height="300" data="' + dd + '" type="application/pdf" width="900"> </object>'
      filo.write(ddx)
      filo.write(ddy)
      k = k+1
filo.write(dd2)
filo.close()
      

