Módulo Numpy
============

Este módulo esta construido de varias clases, principalmente para el
manejo de arreglos.

Ejemplos.

1)

.. code:: Python

   import numpy as np

   a = np.array([1, 2, 3, 4, 5, 6])

   len(a)

   a

   a[0] = 10

   a

   a[:3]

   a[4:]

2)

.. code:: Python

   a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
   a

   a[1, 3]

Atributos de Arreglos
---------------------

.. code:: Python

   a.ndim

   a.shape

   a.shape

   a.dtype

Creando Arreglos Basicos
------------------------

.. code:: Python

   np.zeros(2)

   np.ones(2)

   np.arange(4)

   np.arange(2, 9, 2)

   np.linspace(0, 10, num=5)

Operaciones entre arreglos
--------------------------

.. code:: Python

   x1 = np.linspace(0, 5, num=5)

   x2 = np.array([2,3,2,3,2])

   2*x1

   2*x1-5

   x1*x2

   x1/x2





