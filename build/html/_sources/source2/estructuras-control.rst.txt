Estructuras de Control
======================

Las estructuras de control sirven para dos propositos fundamentales en la programación.

1. Ejecutar una serie de instrucciones en base al valor de una condición.

2. Repetir la ejecución varias veces de una serie de intrucciones.

**Estructura** ``ìf``, ``if-esle``, ``if-elif-else``
 
.. code:: Bash

   if cond:
     inst1
     inst2
     ...
     instn

Si la condición ``cond`` es es distinto de cero entonces ejecuta la serie de instruccioones, de otro modo no las ejecuta.

.. code:: Bash

   if cond:
     inst1
     inst2
     ...
     instn
   else:
     jinst1
     jinst2
     ...
     jinstn 


Si la condición ``cond`` es distito de cero entonces ejecua las in* strucciones de otro modo ejecuta las jin* strucciones.

**Algunos ejemplos**

1)

.. code:: Python

   if 10**(-6):
     print('bien, bien')

.. code:: Python

   if False:
     print('bien, bien')
   else:
     print('mal, mal')

.. code:: Python
     
   if False:
     print('bien, bien')
   elif True:
     print('bien2, bien2')
   else:
     print('mal, mal')
