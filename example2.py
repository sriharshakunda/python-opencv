import cv2
import time
#Read and Load Image

img=cv2.imread('sample.jpg',1)
cv2.imshow('image',img)

#Assign a Specific Key to close all the active windows


while (1):
	k=cv2.waitKey(0)
	if k == ord('e'): # assign key 'e' to exit
		cv2.destroyAllWindows()
		break
		
	else:
		print k # this will print the "DECIMAL" value of they key
	
