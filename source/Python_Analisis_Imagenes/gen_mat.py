import numpy as np
import matplotlib.pyplot as plt

def GenCirculo(ra=0):
  nn = 2*ra+2
  mat = np.zeros((nn, nn))
  
  tt = np.arange(0, 2*np.pi, .01)

  for i in range(nn):
    for j in range(nn): 
      dd = (i-ra)**2 + (j-ra)**2
      if dd <= ra**2:
        mat[i,j] = 1

  return mat

mati = GenCirculo(20)
nn  = mati.shape

img = np.zeros((256, 256))

x0 = 127
y0 = 140

for i in range(nn[0]):
  for j in range(nn[0]):
    img[x0+i, y0+j] = mati[i,j]

plt.imsave("prueba.png", img, cmap="gray")
plt.imshow(img, cmap='gray')

plt.show()

