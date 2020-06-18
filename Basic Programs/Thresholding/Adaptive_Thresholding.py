# Adaptive Thresholding
#we used a global value as threshold value. But it may not be good in all the conditions
#where image has different lighting conditions in different areas.In that case, we go for adaptive thresholding. 
#In this, the algorithm calculate the threshold for a small regions of the image. 
#So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.

#It has three ‘special’ input params and only one output argument.

import numpy as np
import cv2

img= cv2.imread('./images/sudoku_.jpg',0)
_, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 

#C - It is just a constant which is subtracted from the mean or weighted mean calculated.
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11,2)


cv2.imshow('Image',img)
cv2.imshow('Th_Binary',th1)
cv2.imshow('ADAPTIVE_THRESH_MEAN_C',th2)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN_C',th3)



# De-allocate any associated memory usage
cv2.waitKey(0)
cv2.destroyAllWindows()
