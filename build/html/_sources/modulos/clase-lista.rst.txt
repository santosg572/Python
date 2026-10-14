Clase Lista
===========

La clase lista representa un tipo de datos estructurado cuyo elementos de la lista pueden cambiar su valor.

Ejemplos:

.. code:: Python

   l1 = []
   l2 = [1, '1', 2, '2', 3, '3']
   l3 = ['juan' , 'perez']
   l4 = [['juan', 2381053], ['pedro', 2381052]]

**Algunas operaciones en listas**

.. code:: Python

   x = [5, 7, 6, 8, 9, 2, 3, 6, 8]

   x[0]

   x[-1]

   x[2] = 66

   2*x

   x[2:6]




**Métodos de la clase lista:**

``'append', 'clear', 'copy', 'count', 'insert', 'pop', 'remove', 'reverse', 'sort'``

Ejemplos:

.. code:: Python

   x = [1, 3, 2, 2,3,5, 6, 3]

   x.append(99)

   y = x.copy()

   x.count(2)

   x.insert(2, 55)

   x.pop()

   x.remove(3)

   x.reverse()

   x.sort()


