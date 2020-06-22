#Find and Draw Contours with OpenCV in Python -

#Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity. 
#Contours come handy in shape analysis, finding the size of the object of interest, and object detection.
#OpenCV has findContour() function that helps in extracting the contours from the image. 
#It works best on binary images, so we should first apply thresholding techniques

import cv2
import numpy as np

img = cv2.imread('name.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print(contours[0])   #contours gives some array which if we join gives us the boundary of image
#print("Number of Contours found = " + str(len(contours))) 

# Draw all contours 
# -1 signifies drawing all the contours (7 in my case)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3) 

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()


#https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
#Contour Approximation Method 