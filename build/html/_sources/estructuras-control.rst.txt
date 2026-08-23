Estructuras de Control
======================

Valores Lógicos en Python: ``False``, ``True``

Opreradores Lógicos: ``or``, ``and``, 

Ejemplos:

.. code:: Python

   > False and False
   
   > False or False

   > False and True

   > False or True

   > 5 > 5 or "Si" == 'si'

   > 5 >= 5 or "Si" == 'si'
 
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


Si la condición ``cond`` es distito de cero entonces ejecua las ``in*`` strucciones de otro modo ejecuta las ``jin*`` 
instrucciones.

**Algunos ejemplos**

1)

.. code:: Python

   if 10**(-6):
     print('bien, bien')

2)

.. code:: Python

   if False:
     print('bien, bien')
   else:
     print('mal, mal')

3)

.. code:: Python
     
   if False:
     print('bien, bien')
   elif True:
     print('bien2, bien2')
   else:
     print('mal, mal')

**Sentencia:** ``for``

La sentencia "for" se utiliza para iterar sobre los elementos de una secuencia (como una cadena, una tupla o una lista) u otro 
objeto iterable:

.. code:: Python

   for ss in lis:
     ins1
     ins2
     ...
     insn

donde:

* ``ss`` - toma cada valor de la secuencia

* ``lis`` - la secuencia para iterar

* ins1, ins2, ..., insn - conjunto de instrucciones que se ejecutan tantas veces como valores de la lista haya.

**Ejemplos:**

1) 

.. code:: Python

   sum = 0

   for i in range(10):
     sum = sum + i

   print sum

Realiza la suma del 0 al 9, es decir 0+1+2...+9

**Sentencia:** ``while``

La instrucción "while" se utiliza para la ejecución repetida mientras una expresión sea verdadera:

.. code:: Python

   sum = 0
   i = 0     
   for i < 10:
     sum = sum + i
     i = i +1
   print sum

Realiza la suma del 0 al 9, es decir 0+1+2...+9


