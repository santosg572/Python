from deep_translator import GoogleTranslator

dir = './Resp_dic0224'
file = 'fecha_rango_M10D02y24_titulos'

filei = dir + '/' + file + '.txt'
fileo = dir + '/' + file +'_espanol'+'.txt'

fil = open(filei, 'r')
filo = open(fileo, 'w')

datos = fil.readlines()

print(len(datos))

traductor = GoogleTranslator(source='en', target='es')

k = 1
for ss in datos:
  ss = ss.replace('\n', '')
  i = ss.find('"')
  i = ss.find('"',i+1)
  i = ss.find('"',i+1)
  ss = ss[i+1:]
  ln = len(ss)
  ss = ss[:ln-2]
  ss = str(k) + ' : ' + ss + '\n'
  filo.write(ss)
  resultado = traductor.translate(ss)
  filo.write(resultado+ '\n')
  k = k+1
filo.close()



