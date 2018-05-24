import cv2
import numpy as np
def nothing(x):
  pass
cv2.namedWindow('image')
#cap=cv2.VideoCapture('sample.avi',0) -- comment out for video
img=cv2.imread('sample.jpg',0)

def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

#create trackbars for color change
cv2.createTrackbar('low','image',0,255,nothing)
cv2.createTrackbar('high','image',0,500,nothing)

while True:
	#ret,frame=cap.read() -- comment out for video
	blur=cv2.GaussianBlur(img, (5, 5), 0)
	r=cv2.getTrackbarPos('low','image')

	g=cv2.getTrackbarPos('high','Image')

	edges=cv2.Canny(blur, r,g)
	cv2.imshow('image',edges)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()