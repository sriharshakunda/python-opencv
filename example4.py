import cv2
import numpy as np

#Assign varialble for imread
img=cv2.imread('sample.jpg',1)

#Define region of interest (roi) over the image
roi=cv2.rectangle(img,(50,10),(180,40),(0,255,0),3)
cv2.imshow('roi_image',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
