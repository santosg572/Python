import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file = 'cell.jpg'

# 1. Leer la imagen JPG
img = mpimg.imread(file)

imgn = img.copy()

i0 = 30
del1 = 10

imgn[i0:(i0+del1),:,0] = 255
imgn[i0:(i0+del1),:,1] = 0
imgn[i0:(i0+del1),:,2] = 0

# 2. Desplegar la imagen
plt.imshow(imgn)

#plt.axis('off')  # Opcional: oculta los ejes con las coordenadas de píxeles

plt.show()

print(type(img))
print(img.shape)
print(np.max(img))
print(np.min(img))

