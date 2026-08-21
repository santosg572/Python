import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read the image
image = mpimg.imread('prueba.png')

print(type(image))
print(image.shape)

img = image[:,:,0]

nn = img.shape
print(np.min(img))
print(np.max(img))

ix = []
iy = []

for i in range(nn[0]):
  for j in range(nn[1]):
    if img[i,j] > .5:
      ix.append(i)
      iy.append(j)

mat = np.zeros((256, 256))

np = len(ix)

for i in range(np):
  mat[ix[i], iy[i]] = 1

plt.imshow(mat)
plt.axis('off')  # Hide grid lines and axis
plt.show()


