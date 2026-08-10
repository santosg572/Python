Funciones o Métodos
===================

Una función es un programa que tiene argumentos de entrada y resultados de salida. Las funciones se definen con la palabra ``def```.

Ejemplos:

**1)**

.. code:: Python

   def hola():
     print('hola como estas')

   hola()

.. code:: Python

   def hola(var=''):
     print('hola como estas '+ var)

   hola('Pedro')
   hola('Maria')

.. code:: Python

   def X2(x=0):
     return x**2

  X2(4)
  X2(8)

.. code:: Python

   import math
   def Area_Per(radio=0):
     area = math.pi*radio**2
     perimetro = 2*math.pi*radio
     return (area, perimetro)

   res = Area_Per(1)
   print(res)
   print('area = ' + str(res[1]))






