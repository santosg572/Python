Ejemplos
========

.. code:: Python

   import numpy as np
 
   a = np.array([1, 3, 4, 6, 9])

   b = np.array([[1, 2, 3], [4, 5, 6]])

   b2 = np.array([[-1, 2, -3], [4, -5, 6]])

   c =  np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])

Aplicando Métodos

.. code:: Python

   a.shape
   a.size

   b.shape
   b.size 

   c.shape
   c.size 

Sacando datos de los arreglos:

.. code:: Python
   
   x = a[0]

   y = b[1][2]

   z = c[0][1][1]

Aplicando Métodos:

.. code:: Python

   abs(b2)

   b+b2

   np.add(b,b2)

   b.max()

   b.max(1)

   np.append(b,[[7,8,9]],0)

   array([0, 1, 2, 3, 4])

   array([0, 1, 2, 3, 4])


