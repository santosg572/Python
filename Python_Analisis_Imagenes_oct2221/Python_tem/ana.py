#!/usr/bin/env python3

# -*- coding: utf-8 -*-





from PIL import Image, ImageDraw

import numpy as np





def LeeImg(nombre=''):

    jpgfile = Image.open(nombre) 

    print(jpgfile.bits, jpgfile.size, jpgfile.format) 

    image = np.array(jpgfile)

    print(image.shape) 

    img = image[:,:,1] 

    print(img.shape) 

    return np.uint8(img)



def DespliegaImg(img='', let=''):

    print(img.shape)

    imagen = Image.fromarray(img)

    ii = ImageDraw.Draw(imagen)

    ii.text((1,1),let)

 

    imagen.show(title='HOLA')

  



def InvierteImg(img=0):

    x2 = np.max(img)

    x1 = np.min(img)



    img = x2 + x1 - ii

    

    return img





def FiltroMediano(mat=0):

 ss = mat.shape



 imgN = np.zeros(ss)

 for i in range(1,ss[0]-1):

  for j in range(1,ss[1]-1): 

   matt = mat[i-1:i+2, j-1:j+2]

   vec = matt.reshape(-1)

   me = np.median(vec)

   imgN[i,j] = me

 return imgN   



def GeneraRuido(mat=0, por=0):

 ss = mat.shape



 npun = round(ss[0]*ss[1]*por)

 ix = np.round((ss[0]-1)*np.random.uniform(size=npun))

 iy = np.round((ss[1]-1)*np.random.uniform(size=npun))

 

 imgN = mat.copy()



 for i in range(npun):

   imgN[int(ix[i]), int(iy[i])] = 255

 return imgN


