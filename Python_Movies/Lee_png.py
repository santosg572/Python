import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_path = 'frame0417.png'

i1 = 600
i2 = 1100
j1 = 300
j2 = 800

file = 'frame0'

minimos = []
maximos = []

for i in range(1,632):
  if i < 10:
    file2 = file+'00'+str(i)+'.png'
  elif i < 100:
    file2 = file+'0'+str(i)+'.png'
  else:
    file2 = file+str(i)+'.png'  

  image = mpimg.imread(file2)
  img = image[:,:,1]
  img = img[i1:i2, j1:j2]

  mi = np.min(img)
  minimos.append(mi)
  maximos.append(np.max(img))
  
#plt.imshow(img)

plt.plot(minimos) 
plt.plot(maximos)
plt.show()

