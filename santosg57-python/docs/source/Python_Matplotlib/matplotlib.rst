matplotlib-pyplot
=================

**E01**

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 2*np.pi, 300)
   y = np.cos(x)

   plt.plot(x,y)
   plt.show()

**E02**

cardoide.py 

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   teta = np.arange(0, 2*np.pi, .01)

   alfa = 1

   r = alfa * (1 + np.cos(teta))

   x = r * np.cos(teta)
   y = r * np.sin(teta)

   plt.plot(x,y)
   plt.show()


**E03**
   
grafFun01.py 

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   plt.rcParams['text.usetex'] = True 

   latex_title = r"This is a plot of $y = \sin(x)$"
   latex_label = r"$\int_0^1 x^2 dx = \frac{1}{3}$"

   x = np.linspace(0, 2 * np.pi, 400)
   y = np.sin(x)

   plt.plot(x, y)
   plt.title(latex_title)
   plt.xlabel(r"Angle $\theta$")
   plt.ylabel(latex_label)
   plt.text(2, 0.8, r"Max value at $x = \frac{\pi}{2}$", fontsize=12)
   plt.show()

**E04*

fig02.py 

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   def rota(x=0, teta=0):
     rota = np.array([[np.cos(teta), -np.sin(teta)], [np.sin(teta), np.cos(teta)]])
     prod = np.dot(rota,x)
     return prod
 
   t = np.arange(-6.2, 6.2, .01)

   x = 10 * np.sin(2.78 * t)* np.round(np.sqrt(np.cos(np.cos(8.2*t))))
   y = 9*(np.cos(2.78*t))**2 * np.sin(np.sin(8.2*t))

   xy = np.array([x, y]).transpose()

   nn = xy.shape
   print(nn)

   rr = xy[0,:]

   rrn = rota(rr, np.pi/2)
   xyn = np.array([rrn])
   print(xyn.shape)

   for i in np.arange(1,nn[0]):
     rr = np.array(xy[i,:])
   rrn = rota(rr, np.pi/4)
   xyn = np.append(xyn, [rrn], axis=0)

   print(xyn.shape)

   plt.plot(x,y)
   plt.plot(xyn[:,0], xyn[:,1])

   plt.show()
   plt.close()

   plt.show()



