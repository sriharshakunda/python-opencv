#Import neccesary libraries
import cv2
import numpy as np

#assign a variable to imread
img = cv2.imread('sample.jpg',1)

#find region of interest and display the image
roi=cv2.rectangle(img,(50,10),(180,40),(0,255,0),2)
cv2.imshow('region of interest',roi)

#crop roi area and add the cropped region to original image
crop=img[10:40,50:180]
img[100:130,70:200]=crop
cv2.imshow('cropped image',img)

#wait until a key is pressed & destory all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

