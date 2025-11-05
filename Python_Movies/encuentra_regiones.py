import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def EncuentraI0J0():
  global imgB

  nn = imgB.shape
  nx = nn[0]
  ny = nn[1]

  for i in  range(nx):
    for j in range(ny):
       if imgB[i,j] == 1:
          i0 = i
          j0 = j
          break
  return (i0, j0)



def CreceRegion(i0=0, j0=0):
  global imgB
  
  imgB[i0, j0] = 0
  for i in range(i0-1,i0+2):
    for j in range(j0-1,j0+2):
      if imgB[i,j] == 1:
        CreceRegion(i, j) 
  

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


imgB = imgn.copy() 

if np.sum(imgB) > 0:
  r = EncuentraI0J0()

  print(r)

  CreceRegion(r[0], r[1])


#plt.imshow(imgB)
#plt.show()


