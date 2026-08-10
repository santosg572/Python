import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_path = 'cerebro.jpg'  # Replace with the actual path to your JPG file
img = mpimg.imread(image_path)

print(type(img))
print(img.shape)

imgB = img[:,:,0].copy()

print(imgB.shape)

imgB[100:110,:] = 0

i0 = 290
j0 = 370
del1 = 20

imgT = imgB.copy()
muestra = imgT[i0-del1:i0+del1, j0-del1:j0+del1]

me = np.mean(muestra)
sd = np.std(muestra)

print(me)
print(sd)

imgB[i0-del1:i0+del1, j0-del1:j0+del1] = 0

plt.imshow(imgB)

plt.show()


