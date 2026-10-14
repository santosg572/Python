Algunas funciones desarrolladas durante el curso
================================================

# https://en.wikipedia.org/wiki/L-system

**Importar los módulos utilizados**

.. code:: Python

   import numpy as np
   import turtle
   import matplotlib.pyplot as plt
   import matplotlib.image as mpimg
   import pandas as pd

**FUNCIONES**

1)

.. code:: Python

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

2)

.. code:: Python

   def Histograma_Vector(vec=0):
     plt.hist(vec)
     plt.show()

3)

.. code:: Python

   def Despliega_Imagen():
     file = 'corte_sagital.png'
     img = mpimg.imread(file)
     plt.imshow(img)

     # 3. Ocultar los ejes numéricos (opcional)
     plt.axis('off')

     # 4. Mostrar el gráfico
     plt.show()

4)

.. code:: Python

   def estadistica_descriptiva(x=0):
     ''' Calcula algunas medidas descriptivas de la variable "x"

         x - es un vector de tipo array
     '''
     print('media aritmética   : ', np.mean(x))
     print('mediana            : ', np.median(x))
     print('desviación estándar: ', np.round(np.std(x),2))
     print('varianza           : ', np.var(x))

5)

.. code:: Python

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

6)

.. code:: Python

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

7) 

.. code:: Python

   def regresion_lineal(x=0, y=0):
     ''' Realiza una regresión lineal "y" vs "x"

         x, y - son dos vectores numpy
     '''
     m, b = np.polyfit(x, y, 1)

     print(f"Pendiente (m): {m}") 
     print(f"Intersección (b): {b}")

8)

.. code:: Python

   def Grafica_XY(x=0, y=0):
     plt.plot(x, y, 'o')
     plt.show()


9) Múltiples gráficos en una sola ventana

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   # Datos de ejemplo
   x = np.linspace(-10, 10, 100)
   y1 = x
   y2 = x**2
   y3 = x**3
   y4 = x**4

   # Crear una figura y una cuadrícula de 2 filas por 2 columnas
   fig, axs = plt.subplots(2, 2, figsize=(8, 6))

   # Primer gráfico (arriba a la izquierda)
   axs[0, 0].plot(x, y1, color='blue')
   axs[0, 0].set_title('y = x')

   # Segundo gráfico (arriba a la derecha)
   axs[0, 1].plot(x, y2, color='red')
   axs[0, 1].set_title('y = x²')

   # Tercer gráfico (abajo a la izquierda)
   axs[1, 0].plot(x, y3, color='green')
   axs[1, 0].set_title('y = x³')

   # Cuarto gráfico (abajo a la derecha)
   axs[1, 1].plot(x, y4, color='purple')
   axs[1, 1].set_title('y = x⁴')

   # Ajustar automáticamente los espacios entre gráficos
   fig.tight_layout()

   # Mostrar la ventana
   plt.show()


