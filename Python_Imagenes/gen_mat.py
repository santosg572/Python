import numpy as np
import matplotlib.pyplot as plt

mat = np.zeros((256, 256))

print(type(mat))
print(mat.shape)

mat[127,] = 1


ce = (127,127)
ra = 10

tt = np.arange(0, 2*np.pi, .01)

print(tt)

for t in tt:
  ix = int(ce[0] + ra * np.cos(t))
  iy = int(ce[0] + ra * np.sin(t)) 
  mat[ix, iy] = 1

plt.imsave("prueba.png", mat, cmap="gray")
plt.imshow(mat, cmap='gray')

plt.show()

