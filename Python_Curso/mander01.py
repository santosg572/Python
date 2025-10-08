import matplotlib.pyplot as plt
import numpy as np

nx = 500

img = np.zeros((nx+1, nx+1))

xx = np.linspace(-2,2,1000)

niter = 7

for x in xx:
  for y in xx:
    z = float(0)
    c = complex(x,y)
    for i in range(niter):
      z = z**4 +c
    if abs(z) < 1000:
      ix = int(nx*(x+2)/4)
      iy = int(nx*(y+2)/4)
      img[ix, iy] = 255

plt.imshow(img)
plt.show()

