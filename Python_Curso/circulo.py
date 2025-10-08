import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((256,256))

img[50,:] = 255

te = np.arange(0, 2*np.pi,.1)

x0 = 50
y0 = 70

x = np.int32(x0 + 10*np.cos(te))
y = np.int32(y0 + 10*np.sin(te))

for i in range(len(x)):
  img[x[i], y[i]] = 255

plt.imshow(img)
plt.show()



