from matplotlib import pyplot as plt 
import cv2
import numpy as np 

def DesImg(img=0):
	while True:
		cv2.imshow('result', img)
		if cv2.waitKey(1) & 0xFF == 27:
			break

def DesHist(vec):
	plt.hist(vec, bins=list(range(0, 255,10)))
	plt.title("histogram2")
	plt.show()

def Diferencia_Imgs(img1=0, img2=0):
	nn = img1.shape
	img3 = img1 - img2
	for i in range(nn[0]):	
		for j in range(nn[1]):
			img3[i,j] = abs(img3[i,j])
	return img3


fil1 = "file163.png"
fil2 = "file164.png"
img1 = cv2.imread(fil1)
img2 = cv2.imread(fil2)

img1 = img1[:,:,0]
img2 = img2[:,:,0]

img12 = Diferencia_Imgs(img1, img2)
nn = img12.shape

vec = img12.reshape(nn[0]*nn[1],1)
print(vec.shape[0])

print(type(vec))


#DesHist(vec)

imgB = 255.*(img12 < 50)
print(imgB.shape)

DesImg(img1)



