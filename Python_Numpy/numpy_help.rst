Help numpy
==========

**Ejemplos**

1)

.. code:: Python

   import numpy as np
   
   a = np.array([[3,2,3,5],
                 [2,3,3,4]])

   np.amax(a)

   np.amax(a,0)

   b = np.append(a,[[1,6,2,3]],axis=0)

   np.apply_along_axis(np.mean,0, b)

2)

.. code:: Python

   x = np.arange(-5,5)

   y = np.arange(0, 2*np.pi, .1)

3)

.. code:: Python

   import numpy as np

   teta = np.pi/2

   np.sin(teta)

   np.cos(teta)

   np.arctan(1)

4)

.. code:: Python

   x = np.array([4,2,3,4,6,3,4])

   x.argmax()

   x.max()

   x.mean()

   x.var()

   x.std()

   np.median(x)

   np.cumsum(x)

 **Algunas Distribuciones**

**Ejemplos**

1)

.. code:: Python

   import numpy.random as rr

   rr.binomial(1, .8, size=3)

   rr.chisquare(.3,10)

   rr.exponential(1,10)

   rr.normal(55, 7, 10)

   rr.poisson(1, 10)

   rr.randint(1,100, 10)

   rr.randn(5)

   rr.random(10)




