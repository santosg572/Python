Creando Imágenes
================

El siguiente codigo crea una imagen y la salva en disco.

.. code:: Python

   import matplotlib.pyplot as plt
   import matplotlib.image as mpimg
   import numpy as np

   img = np.zeros((256,256))

   for i in range(255):
     img[i,i] = 1

   teta = np.linspace(0, np.pi/2, 5)

   for te in teta:
     for i in range(255):
       j = (int)(np.tan(te)*i)
       if (0 <= j) and (j <=255):
         img[i,j] = 1

   plt.imshow(img, cmap='gray')

   plt.savefig('imagen_matriz.jpg')

   plt.show()




