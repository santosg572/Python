TAREA 02. Para entregar el próximo lunes 
========================================

* 1. Hacer una función en Python para que calcule el factorial de un número natural.

* 2. Utilizando la función factorial, hacer una función que dado un número natural y un número :math:`x \in R` calcule la serie:

.. math::

   S =  1 + x + \frac{x^2}{2!} +  \frac{x^3}{3!} +  \frac{x^4}{4!} + ... +  \frac{x^{100}}{100!}

3. Genere la serie de Fibonacci haste que el último número de la serie no sea mayor que 1000.

Se define como sigue:

a) Comienza con el 0 y el 1

b) Se suman las dos cifras previas para obtener la siguiente:

* 0 + 1 = 1
* 1 + 1 = 2
* 1 + 2 = 3
* 2 + 3 = 5
* 5 + 3 = 8
* 8 + 5 = 13
 
c) La secuencia avanza así: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

4. Grafique el L-Sistema definido como sigue:

* variables  : FG
* constantes  : + −
* inicio   : F − G − G
* Reglas   : (F → F − G+F+G − F), (G → GG)
* ángulo   : 120°

Aquí, F y G significan "avanzar", + significa "girar a la izquierda el ángulo" y − significa "girar a la derech el ángulo".
 
5. Dadas las ecuaciones parametricas de un círculo. Encontrar el perímetro del círculo  tomando varios valores de 
:math:`\theta \in [0, 2\pi]` y sumado las distancia entre los puntos que definen los :math:`\theta`s.

.. math::

   x = 2 \sin \theta

   y = 2 \cos \theta

 
para :math:`\theta \in [0, 2\pi]`


6. Dibujar 50 círculos aleatorios en la ventana de tamaño [-200, 200] x [-200, 200] de radio aleatorio entre 10 y 20 
unidades inclusive. Utilice la función ``circle`` del módulo turtle.






