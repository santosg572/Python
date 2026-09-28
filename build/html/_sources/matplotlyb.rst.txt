Matplotlib.pyplot
=================

**Ejemplos**

1)

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 4*np.pi, .1)

   y1 = np.sin(x)

   plt.plot(x,y1)

   plt.show()

2)


.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 4*np.pi, .1)

   y1 = np.sin(x)
   y2 = 2*y1

   plt.plot(x,y1, x, y2)

   plt.show()

3)

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.array([4, 5, 6, 5, 6,6,7,5,5,8])

   plt.hist(x)
   plt.show()

4)

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.array([4, 5, 6, 5, 6,6,7,5,5,8])
   
   plt.bar(np.arange(10), x)
   plt.show()

5)

.. code:: Python

   import numpy as np
   import matplotlib.pyplot as plt

   x = 7*np.random.randn(10)+55
   y = 9*np.random.randn(10)+60
   z = 4*np.random.randn(10)+57

   plt.boxplot((x,y,z))

   plt.show()

