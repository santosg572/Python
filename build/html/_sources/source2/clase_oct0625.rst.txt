Clase-oct0625
=============

   * Módulo ``matplotlib``
   * Módulo ``pandas``

ejemplo01

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.int32(np.random.normal(55, 10, 100))
   print(x)

   ax1 = plt.subplot(2, 2, 1)

   ax1.plot(x, 'o')
   ax1.title.set_text('Números aleatorio')

   ax2 = plt.subplot(2, 2, 2)
   ax2.hist(x)
   ax2.title.set_text('Histograma')

   ss = set(x)
   print(ss)

   dd = dict()

   for i in np.arange(len(ss)):
     cc = ss.pop()
     dd[cc] = 0

   for xx in x:
     dd[xx] = dd[xx]+1

   print(dd)

   x1 = list(dd.keys())
   y1 = list(dd.values())

   print(x1)
   print(y1)

   ax3 = plt.subplot(2, 2, 3)
   ax3.plot(x1, y1, 'or')

   ax3 = plt.subplot(2, 2, 4)
   ax3.boxplot(x)

   print('media= ',np.mean(x))
   print('mediana= ',np.median(x))
   print('mínimo= ',np.min(x))
   print('max= ',np.max(x))
   print('desviación estándar= ',np.std(x))
   print('varianza= ',np.var(x))

   plt.show()


Ejemplo02

.. code:: Python

   import matplotlib.pyplot as plt
   import pandas as pd

   datos = pd.read_csv('datos.csv')


   print(datos)

   print(datos.describe())

   datos.boxplot()

   plt.show()





