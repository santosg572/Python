# https://en.wikipedia.org/wiki/L-system

import numpy as np
import turtle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def Histograma_Imagen():
  file = 'corte_sagital.png'
  img = mpimg.imread(file)
  imgb = img[:,:,0]
  print(np.max(imgb))
  print(np.min(imgb))
  imgb = 100*imgb / np.max(imgb)
  si = img.shape
  print(si)
  vec = imgb.reshape(si[0]*si[1])
  print(vec.shape)
  ii = np.arange(0,100,1)
  plt.hist(vec, ii)
  plt.show()

def Despliega_Imagen():
  file = 'corte_sagital.png'
  img = mpimg.imread(file)
  plt.imshow(img)

  # 3. Ocultar los ejes numéricos (opcional)
  plt.axis('off')

  # 4. Mostrar el gráfico
  plt.show()

def estadistica_descriptiva(x=0):
  ''' Calcula algunas medidas descriptivas de la variable "x"

      x - es un vector de tipo array
  '''
  print('media aritmética   : ', np.mean(x))
  print('mediana            : ', np.median(x))
  print('desviación estándar: ', np.round(np.std(x),2))
  print('varianza           : ', np.var(x))

def Curva_de_Koch():
  si = 'F'
  regla = 'F+F-F-F+F'
  teta = 90

  niter = 3
  for i in range(niter):
    ss = si.replace('F', regla)
    si = ss

  for s in si:
    if s == 'F':  
      turtle.fd(10)
    elif s == '+':
      turtle.left(90)
    else:
      turtle.right(90)
  turtle.mainloop()

def triangulo_de_sierpinski():
  si = 'F-G-G'
  r1 = 'F-G+F+G-F'
  r2 = 'GG'
  teta = 120

  niter = 2
  for i in range(niter):
    ss = ''
    for s in si:
      if s == 'F':
        ss = ss + r1
      elif s == 'G':
        ss = ss + r2
      else:
        ss = ss+s
    si = ss
  
  for s in si:
    if s in ['F', 'G']:
      turtle.fd(10)
    elif s == '+':
      turtle.left(teta)
    else:
      turtle.right(teta)
  turtle.mainloop()

def regresion_lineal(x=0, y=0):
  ''' Realiza una regresión lineal "y" vs "x"

      x, y - son dos vectores numpy
  '''
  m, b = np.polyfit(x, y, 1)

  print(f"Pendiente (m): {m}") 
  print(f"Intersección (b): {b}")


def Grafica_XY(x=0, y=0):
  plt.plot(x, y, 'o')
  plt.show()





