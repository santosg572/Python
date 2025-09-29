numpy 
=====

help_abs.txt

**abs**

Calcula el valor absoluto de cada elemento del arreglo.

.. code:: Python

   a = np.array([[-2,2,-3],[1,-3,-4]])
   a

   b=np.abs(a)
   b 

   b[0,0]=-6
   b

.. code:: Python

   np.abs(1.2 + 1j)

**amax**

Regresa el maximo de un arreglo o maximo a lo largo de un eje.

.. code:: Python

   a = np.array([[2,3,4], [3,2,4]])
   a
   np.amax(a)

   np.amax(a, 0)

   np.amax(a, 1)


**append**

Añade valores al final de un  arreglo

append(arr, valores, axis)

.. code:: Python

   a
   array([[2, 3, 4],
       [3, 2, 4]])
   b = np.append(a, [[6,7,8]],0)
   b

   f=np.array([[9],[10],[11]])
   k = np.append(b,f,1)
   k


**apply_along_axis**

apply_along_axis(func1d, axis,

Aplica una funcion a lo largo del eje

.. code:: Python

   b
   array([[2, 3, 4],
       [3, 2, 4],
       [6, 7, 8]])

   np.apply_along_axis(np.mean,0,b)

**arange**

arange([start,] stop[, step,],

Regresa valores espaciados en un intervalo dado

.. code:: Python

   np.arange(3.0)

   np.arange(3,7)

   np.arange(3,7,2)

**around**

Redondea el numero dado de decimales

.. code:: Python

   np.around([0.37, 1.64])

   np.around([0.37, 1.64], decimals=1)

**array**

Crea un arreglo

array(object, dtype=None

.. code:: Python

   np.array([1, 2, 3.0])

   np.array([[1, 2], [3, 4]])


**linspace**

Regresa numeros espaciados sobre un intervalo dado

linspace(start, stop, num=50, 

.. code:: Python

   np.linspace(2.0, 3.0, num=5)


**ones**

Regresa un arreglo de unos.

ones(shape, dtype=None,

.. code:: Python

   np.ones(5)

   np.ones((2, 1))

**zeros**

Regresa un arreglo de ceros.

zeros(shape, dtype=float,

.. code:: Python

   np.zeros(5)

   s = (2,2)

