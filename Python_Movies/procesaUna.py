import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

i1 = 600
i2 = 1100
j1 = 300
j2 = 800

file = 'frame0'

i = 1
if i < 10:
    file2 = file+'00'+str(i)+'.png'
elif i < 100:
    file2 = file+'0'+str(i)+'.png'
else:
    file2 = file+str(i)+'.png'  

image = mpimg.imread(file2)
img = image[:,:,1]
img = img[i1:i2, j1:j2]

imgn = img < .5

nn = imgn.shape
nx = nn[0]
ny = nn[1]

print(nx*ny)

suma = 0
for i in  range(nx):
  for j in range(ny):  
     if imgn[i,j] == 1:
        suma = suma+1
        imgn[i,j] = 0 

print(suma)
plt.imshow(imgn)

#plt.plot(minimos) 
#plt.plot(maximos)
plt.show()

