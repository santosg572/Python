Clase Lista
===========

La clase lista representa un tipo de datos estructurado cuyo elementos de la lista pueden cambiar su valor.

Ejemplos:

.. code:: Bash

   l1 = []
   l2 = [1, '1', 2, '2', 3, '3']
   l3 = ['juan' , 'perez']
   l4 = ['juan', 2381053], ['pedro', 2381052]]

Métodos de la clase lista:

``'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'``

Ejemplos:

.. code:: Bash

   l1 = []
   l1.append(['María', 2434234])
   len(l1)
   l1

.. code:: Bash

   x = [1,3,2,4,5,4,7,4,5,4]
   x,count(4)

Consideremos el siguiente texto:

   How big is a fractal? When are two fractals similar to one another in some sense? What experimental measurements 
might we make to tell if two different fractals may be metrically equivalent? What is the same about the two fractals 
in Figure V.131?

There are various numbers, associated with fractals, which can be used to compare them. They are generally referred to 
as fractal dimensions. They are attempts to quantify a subjective feeling we have about how densely the fractal 
occupies the metric space in which it lies. Fractal dimensions provide an objective means for comparing fractals.

Ejemplos:

.. code:: Bash

   x = x.replace('\n', ' ')
   y = x.split(' ')
   type(y)
   y.remove('V.131?')
   y.pop()
   y.index('When')
   y.sort()


