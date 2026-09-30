import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file = 'cell.jpg'

# 1. Leer la imagen JPG
img = mpimg.imread(file)

# 2. Desplegar la imagen
plt.imshow(img)

plt.show()

