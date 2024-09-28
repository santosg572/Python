import cv2
import numpy as np 

fil1 = "file163.png"
fil2 = "file164.png"
img1 = cv2.imread(fil1)
img2 = cv2.imread(fil2)

img1 = img1[:,:,0]
img2 = img2[:,:,0]

print(img1.shape)

while True:
	cv2.imshow('result', img1)
	if cv2.waitKey(1) & 0xFF == 27:
		break


