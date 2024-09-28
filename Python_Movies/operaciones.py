import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

nimages = 260

def Maximo(file1='', file2=''):
 image1 = mpimg.imread(file1)
 image2 = mpimg.imread(file2)
 image1 = image1[:, :, 1]
 image2 = image2[:, :, 1]
 image3 = np.abs(image1 - image2)
 ss = image3.shape
 nx = ss[0]
 ny = ss[1]

 vec = image3[0,:]

 for i in np.arange(1, nx):
  vec = vec + image3[i,:]
 vec = vec / nx
 return np.max(vec)

f1 = 'file1.png'

mm = []
for i in np.arange(2,261):
 f2 = 'file'+str(i)+'.png'
 m = Maximo(f1, f2)
 f1 = f2
 print(m)
 mm.append(m)

plt.plot(mm)

#plt.imshow(mm)
plt.show()


