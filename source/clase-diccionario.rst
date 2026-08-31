clase diccionario
=================

Un diccionario en Python es una estructura de datos mutable que guarda información en pares de clave y valor 
**(key: value)**.

**Características principales**

* **Mutables:** Se pueden agregar, modificar y eliminar elementos después de 
crearlos.

* **Claves únicas:** Cada clave dentro del diccionario no se puede repetir y debe ser de un tipo 
inmutable (como cadenas o números).

* **Sin orden numérico:** Los elementos no se buscan por una posición o índice 
numérico, sino por su nombre de clave

**Creación y uso básico**

Se definen utilizando llaves ``{}`` separando la clave del valor con dos puntos

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


   

