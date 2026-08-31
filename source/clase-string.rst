Clase String
============

Un string es una secuencia de caracteres o formado de varias 
linas de caracteres encerradaos por los simbolos: ' ó ".

Ejemplos:

1) 

.. code:: Python

   'Juan Peréz'

2)

.. code:: Python

   "Juan Peréz"

3)

.. code:: Python

   '''Hola como estas,
      yo me encuentro bien,
      saludos.'''


Dada la variable string: ``x = 'hola como estas'``

Podemos hacer lo siguiente:

* ``x[0]``  # muestra el primer caracter
   
* ``x[-1]`` # muestra el ultimo caracter

* ``x[:3]`` # muestra los dos primeros caracteres

* ``x[5:]`` # muestra los caracteres a partir de la posicion 5

* ``x[3:10]`` # muestra los caracteres en las posiciones, 3, 4, 5, 6, 7, 8 y 9    

* ``2*x`` # crea un string formado al repetir dos veces el string x
   
* ``x + x + x`` # crea un string formado al repetir tres veces el string x


**Algunos métodos de la clase string:**


``'capitalize', 'count', 'find', 'index', 'isalpha', 'isdigit', 'lower', 'replace', 'rfind', 'rindex', 'split', 'translate', 'upper'``

**Ejemplos**

Consideremos el siguiente string y apliquemos algunas funciones:

.. code:: Python

   x = ''' Mi nombre es Leopoldo,
           vido actualmente en Queretaro,
           mi novia se llama Olivia y vide 
           en la Ciudad de Mèxico'''

* ``x.capitalize()`` # convierte las letras a mayusculas

* ``x.count('en')`` # cuenta cuantas veces se repite el string **en**

* ``x.find('en')`` # en que posición se encuentra el string **en**, a partir del caracter inicial, regresa 
cero 
si no lo encuentra.


* ``x.find('en', 48)`` # inicia la busqueda a partir de la posción 48

* ``x.isalpha()`` # el string esta formado de caracteres alfabeticos, si es verdadero regresa ``True``

* ``x.lower()`` # convierte las letras a minúsculas

* ``x.replace('Mi', 'my')`` # replaza todas las ocurrencias del string **Mi** por el string **my**

* ``x.split('\n')`` # cre una listas de string's cuyo separador es el string cambio de linea.



