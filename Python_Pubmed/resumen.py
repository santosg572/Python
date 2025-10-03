import sys

archivo  = sys.argv[1]

fileo = open(archivo+'O.txt', 'w')

with open(archivo+'.txt') as archivo:
 for linea in archivo:
  if 'abstract' in linea:   
   linea = linea.replace('\n', ' ')
   fileo.write(linea)
   fileo.write('\n')
fileo.close()




