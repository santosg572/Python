import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file = 'cell.jpg'

# 1. Leer la imagen JPG
img = mpimg.imread(file)

imgB = img[:,:,0].copy()

i0 = 160
j0 = 400

del1 = 60

imgB[(i0-del1):(i0+del1), j0] = 255
imgB[i0, (j0-del1):(j0+del1)] = 255

imgB = imgB[(i0-del1):(i0+del1), (j0-del1):(j0+del1)]

plt.imshow(imgB, cmap='gray') 

#plt.axis('off')  # Opcional: oculta los ejes con las coordenadas de píxeles

plt.show()

print(type(imgB))
print(imgB.shape)
print(np.max(imgB))
print(np.min(imgB))

