import cv2
raw = cv2.VideoCapture('IMG_7687.MOV')
 
while 1:
    ret,frame = raw.read()
    cv2.imshow('hsv',frame)
    cv2.waitKey(10)


