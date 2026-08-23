Listas
======

Una lista es una estructura de datos.

Algunos ejemplos

.. code:: Python

   x = [1,2,33,5,6,7,8]
   
   y = []

.. code:: Python

   z = 'dasda123'
   z = list(z)
   z

Algunos methodos:

**'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 
'sort'**

Ejemplos:

Consideremos el siguiente texto:


The fly’s genetic tools to label and manipulate neurons havebeen extensively used to characterize single 
cells or circuitsof a few neurons involved in specific functions. However, itremains unclear how specific 
temporal activity patterns inneurons affect circuit function, and how different circuitsinteract with each 
other to guide coherent outcomes such asbehavior. Some properties might also emerge at a more glo-bal level 
from synergistic or antagonistic interactions ofmany neurons or small circuits in a way that cannot be 
pre-dicted when considering individual elements. Hence, on topof studying all or none effects by manipulating 
individualneurons in behavioral assays, which can have the advantageof being performed with high throughput 
in freely behavinganimals, it is important to study the dynamics of popula-tions of neurons, even if this has 
so far only been achievedin head-fixed dissected flies.One simple example of how dynamical propertiesstrongly 
shape information propagation is the concept ofresonance. An oscillating system, such as a pendulum, 
willrespond very differently when excited by inputs of differentrhythms. Some input frequencies will induce 
very littleresponse, yet the right frequency will lead to large oscilla-tions, indicating a strong 
transmission of energy. Whenmore than two dynamical elements interact, the resultingdynamics becomes harder 
to understand and predict. Thefield of complexity and dynamical systems (as exemplifiedbelow) helps 
understand the properties of such systems.

Ejemplos:

.. code:: Python

   type(xx)

   len(xx)

   xx = xx.replace('\n','')
   y1 = xx.split(' ')
   type(y1)
   len(y1)

   palabras=set(y1)
   type(palabras)
   len(palabras)

   palabras=list(palabras)
   type(palabras)
   len(palabras)

   palabras.sort()

   palabras.remove('(as')

   palabras.pop()

   palabras.index('littleresponse,')

   palabras.index('oscilla-tions,')

   palabras.insert(112, 'oscillations')


