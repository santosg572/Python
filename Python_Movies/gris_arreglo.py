import cv2
import numpy as np
from PIL import Image

raw = cv2.VideoCapture('IMG_7687.MOV')

k = 0 
while 1:
	ret,frame = raw.read()
	try:
		k = k+1
		image = np.asarray(frame)
		file = 'file'+str(k)+'.png'
		print(file)
		Image.fromarray(image).save(file)
		print(np.shape(image))
		cv2.imshow('hsv',frame)
		cv2.waitKey(10)
	except:
		print("Here")
		break

print('termino bien')
print(k)

