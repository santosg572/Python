import numpy as np
import matplotlib.pyplot as plt

x1 = -4
x2 = 6

x = np.linspace(x1, x2, 1000)

y = np.sin(x)

img = np.zeros((256, 256))

np1 = len(x)

for i in range(np1):
  xx = x[i]
  yy = y[i]
  ix = int((xx-x1)*255/(x2-x1))
  iy = int((yy - 2)*255/4)
  img[ix, iy] = 255

plt.imshow(img)
#plt.plot(x,y)
plt.show()




