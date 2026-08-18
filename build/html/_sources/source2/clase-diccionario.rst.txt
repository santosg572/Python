clase diccionario
=================

Es un tipo de dato estructurado cuyos datos se manejan con llaves, es decir 
para cada dato esta indentificado por una llave.

Ejemplos.

1) Diccionario vacío

.. code:: Python

   x = dict()
   type(x)

2) Diccionario con tres llaves y sus respectivos valores.

.. code:: Python

   y = {'pesos':[45, 64, 70], 'edad': 65, 'nombres': ('Juan', 'Pedro')}
   type(y)

Desplegando datos del diccionario.

Consideremos el siguiente diccionario:  y = {'pesos':[45, 64, 70], 'edad': 65, 'nombres': ('Juan', 'Pedro')}.
Entonces:

.. code:: Python

   y
  
   y['nombres']

   y['nombres'][1]

Algunos métodos:

``'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'``


   

