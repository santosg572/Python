Método plot
===========

Ejemplos

1)

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt
   x=np.arange(0, 10, .1)
   y1 = np.sin(x)
   y2 = np.sin(x+.5)
   plt.plot(x,y1)
   plt.plot(x,y2)
   plt.show()

Tarea: Graficar la siguiente función en el intervalo [-5,5]

.. math::

   \varphi_{\mu, \sigma^2}(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x-\mu)^2}{2 \sigma^2} }


Para a) :math:`\mu=0, \sigma=1` y b)  :math:`\mu=55, \sigma=5`
