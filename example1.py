import cv2

#Assign Variable to read image file

img=cv2.imread('sample.jpg',1) # 0 for Grey and 1 for color

#Load image and Open it using imshow fuction

cv2.imshow('image',img)

#Wait until a key is pressed and close all the active windows

cv2.waitKey(0)
cv2.destoryAllWindows()
