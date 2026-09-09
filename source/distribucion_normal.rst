Distribución normal
===================

https://es.wikipedia.org/wiki/Distribuci%C3%B3n_normal

En estadística y probabilidad se llama distribución normal, distribución de Gauss, distribución gaussiana a una gráfica de función de 
densidad con forma acampanada y simétrica respecto de un determinado parámetro estadístico. Esta curva se conoce como campana de Gauss y es 
el gráfico de una función gaussiana.[1][2] Su forma general es:

.. math::

   f(x)= \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \text{ en } -\infty < x < \infty


.. image:: graf_normal.png

.. code.. Python

   import numpy as np
   import matplotlib.pyplot as plt

   mu = 55
   sd = 10

   x = np.linspace(mu-4*sd, mu+4*sd, 100)

   ex = (x - mu)**2/(2*sd**2)

   y = np.exp(-1*ex) / np.sqrt(2*np.pi*sd**2)

   plt.plot(x,y)
   plt.show()


