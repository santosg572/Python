Clase tupla
===========

En Python, una tupla es una estructura de datos ordenada que permite almacenar varios elementos en una sola variable. Su característica principal es que es inmutable: una vez creada, no se puede modificar, añadir ni eliminar ningún elemento. Se escriben usando paréntesis ().

**Características principales**

* **Inmutabilidad:** No puedes cambiar sus valores ni usar métodos como ``append()`` o ``remove()``.
* **Ordenadas:** Los elementos mantienen una posición fija y seToIndexan desde el 0.
* **Heterogéneas:** Pueden contener datos de distintos tipos (números, textos, booleanos u otras estructuras).
* **Eficientes:** Ocupan menos memoria y son más rápidas que las listas.

**Cómo crear y usar tuplas**

* **Crear una tupla:** `` mi_tupla = (1, "Hola", 3.14)`` o simplemente ``otra_tupla = 1, 2, 3`` (sin paréntesis).
* **Tupla de un solo elemento:** Requiere una coma final obligatoria: elemento_unico = (5,).
* **Acceder a elementos:** Se usan corchetes con el índice, por ejemplo mi_tupla[0] para el primer elemento o índices negativos como mi_tupla[-1] para el último.
* **Métodos disponibles:** Solo tienen dos métodos integrados principales: ``.count()`` (cuenta cuántas veces aparece un valor) y ``.index()`` (devuelve la posición de un valor).


La clase tutpla representa un tipo de datos estructurado, cuyos elementos no pueden ser modificados.

Ejemplos:

.. code:: Bash

   x = ()
   type(x)
   
Métodos de la clas tupla:

``'count', 'index'``
 
Ejemplos:

.. code:: Bash

   y = ('a', 'b', 'c', 'a', 'b', 'a', 'c')
   len(y)
   y.count('b')
   y.index('b')





