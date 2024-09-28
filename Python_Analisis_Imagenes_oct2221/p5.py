#http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#functions

from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

jpgfile = Image.open("cuadrado.jpg")
print dir(jpgfile)

print jpgfile.bits, jpgfile.size, jpgfile.format

image = np.array(jpgfile)
ss = image.shape
print ss
print ss[0]*ss[1]

img = image # image[:,:,1]
print img.shape

#img = 255 * (img > 10) * (img<50)

img = 255 * (img > 50) * (img < 80)

im = Image.fromarray(np.uint8(img))
im.show()


