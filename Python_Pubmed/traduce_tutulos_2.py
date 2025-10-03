from deep_translator import GoogleTranslator
import sys

#print(sys.argv)

file = sys.argv[1]
print(file)


filein = file + "_title"

fileon = filein +'_espanol'+'.txt'

fil = open(filein+'.txt', 'r')
filo = open(fileon, 'w')

datos = fil.readlines()
fil.close()

print(len(datos))

traductor = GoogleTranslator(source='en', target='es')

k=1
for pal in datos:
  ln = len(pal)
  xx = pal[13:ln-2]
  resultado = traductor.translate(xx)
  filo.write(str(k)+ '  ' + pal+'\n')
  filo.write(resultado+'\n\n')
  k = k+1

filo.close()

