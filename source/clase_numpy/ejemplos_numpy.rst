Ejemplos 
========

**1)**

.. code:: Python

   import numpy as np

   x = np.array([3,2,4,3,5,3,6,2])

   x.dtype

   x.size

   x.itemsize

   x.nbytes

   x.ndim

   x.shape

**2)**

.. code:: Python

   mat = np.array([[4,3,2],[1,2,3], [5,6,8]])

   mat.T

   mat.dtype

   mat.size

   mat.itemsize

   mat.nbytes

   mat.ndim

   mat.shape

   
**3)**

.. code:: Python

   mat0 = np.zeros((3,4))

   mat1 = np.ones((3,2))
 
   mat3 = np.ones((3,2, 4))
   
**Sacando elementos de un arreglo**

**4)**

.. code:: Python

   x = np.array([2,1,3,2,1,4,5,6,4])

   x[2]

   x[(3, 6)]

   x[[3, 6]]

   x[x == 2]

   x[x>=3]

**5)**

.. code:: Python

   mat = np.array([[1,2,4,2,3,2,5],[2,3,4,5,3,3,5],[1,6,4,5,3,1,2]])

   mat[1,3]

   mat[1,]

   mat[:,2]

   mat[1:3,5]

   mat*(mat>3)

**Operaciones en matrices**

.. code:: Python

   2*x+1

   np.sqrt(x)

   x**2

   np.log(x)

**6)**

.. code:: Python

   import numpy as np

   np.random.randn(20)

   x = 10*np.random.randn(20)+55

   y = np.round(x)

   z = np.round(8*np.random.randn(20)+60)

   y+z

   y - z
  
   y**2

   y/z

   

