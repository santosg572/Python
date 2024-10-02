#http://pillow.readthedocs.io/en/3.4.x/reference/Image.html#functions

from PIL import Image, ImageDraw
import numpy as np


def LeeImg(nombre=''):
    jpgfile = Image.open(nombre) 
    print(dir(jpgfile)) 
    print(jpgfile.bits, jpgfile.size, jpgfile.format) 
    image = np.array(jpgfile)
    print(image.shape) 
    img = image[:,:,1] 
    print(img.shape) 
    return img



ii = LeeImg('download.jpg')

im = Image.fromarray(np.uint8(ii))
im.show()






