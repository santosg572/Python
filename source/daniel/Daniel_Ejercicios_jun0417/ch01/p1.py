import numpy as np
import random

def LeeArchivo():
  file = 'EXA_C01_S04_01.csv'

  fil = open(file, 'r')

  datos = fil.readlines()

  edad = list()

  datos = datos[1:]

  for ss in datos:
    ss = ss.replace('\n','')
    s1 = ss.split(',')
    num = float(s1[1])
    edad.append(num)
  return edad

def EstdisticaDescriptiva(x = 0):
  print('media: ', np.round(np.mean(x),2))
  print('media: ', np.median(x))
  print('desviación estandar: ', np.round(np.std(x),2))
  print('varianza: ', np.round(np.var(x),2))


def frecuencia(x, n1=0, n2=0):
  num = 0

  for i in x:
    if n1 <= i and i < n2:
      num = num + 1
  return num



age = LeeArchivo()

print(age)

EstdisticaDescriptiva(age)

muestra = random.sample(age, 12)

print('ESTADISTICA DESCRIPTIVA DE LA MUESTRA')

print(muestra)

print(EstdisticaDescriptiva(muestra))


clas1 =  frecuencia(age, n1=30, n2=40)
clas2 =  frecuencia(age, n1=40, n2=50)
clas3 =  frecuencia(age, n1=50, n2=60)
clas4 =  frecuencia(age, n1=60, n2=70)
clas5 =  frecuencia(age, n1=70, n2=80)
clas6 =  frecuencia(age, n1=80, n2=90)

print(clas1)
print(clas2)
print(clas3)
print(clas4)
print(clas5)
print(clas6)

frec = np.array([clas1, clas2, clas3, clas4, clas5, clas6])

print(frec)

print(np.cumsum(frec))









