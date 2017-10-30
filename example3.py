import cv2

#Read Image File
img=cv2.imread('sample.jpg',0) # 0 to change image from color to grey

#Assign 'e' to exit and 's' to save and exit
cv2.imshow('image',img)
while (1):
	k = cv2.waitKey(0)
	if k == ord('e'):
		print ("Closing Image")
		cv2.destroyAllWindows()
		break
	elif k == ord('s'):
		print("Saving Image")
		cv2.imwrite('example3_output.jpg',img)
		cv2.destroyAllWindows()
		break
	else:
		print k
