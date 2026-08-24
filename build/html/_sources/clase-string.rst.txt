Clase String
============

Un string es una secuencia de caracteres o formado de varias linas de caracteres encerradaos por los simbolos: ' o ".

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

Definamos la siguientes variables string y podemos hacer los siguiente:

.. code:: Python

   x = 'hola como estas'

   x[0]  # muestra el primer caracter
   
   x[-1] # muestra el ultimo caracter

   x[:3] # muestra los dos primeros caracteres

   x[5:] # muestra los caracteres a partir de la posicion 5

   x[3:10] # muestra los caracteres en las posiciones, 3, 4, 5, 6, 7, 8 y 9    

   2*x # crea un string formado al repetir dos veces el string x
   
   x + x + x # crea un string formado al repetir tres veces el string x


**Algunos métodos de la clase string:**


``'capitalize', 'count', 'find', 'index', 'isalpha', 'isdigit', 'lower', 'replace', 'rfind', 'rindex', 'split', 'translate', 'upper'``

**Ejemplos**

Consideremos el siguiente string y apliquemos algunas funciones:

.. code:: Python

   x = ''' Mi nombre es Leopoldo,
           vido actualmente en Queretaro,
           mi novia se llama Olivia y vide 
           en la Ciudad de Mèxico'''

   x.capitalize()

   x.count('en')

   x.find('en')

   x.find('en', 48)

   x.isalpha()

   x.lower()

   x.replace('Mi', 'my')

   x.split('\n')


