#Simple Image Thresholding- In computer vision image segmentation is the base for analysing images by converting an image into multiple segments (super pixel) or regions.
#Image thresholding is one of the simplest method to separate regions which are higher than the set threshold.

#Thresholding means converting image into binary format. 
#It is important for image processing. Because, some time people need separation of dark and light region. 
#Thresholding image can separate dark and light side of the colorful image.

import cv2
import numpy as np
from matplotlib import pyplot as plt


img= cv2.imread('gradient.jpg',0)
#img= cv2.resize(img,(350,350))

# applying different thresholding techniques on the input image 

# All pixels value above 120 will be set to 255 in simple THRESH_BINARY and so features of other types.
_, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 
_, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #inverse of Binary
_, th3 = cv2.threshold(img, 150, 255, cv2.THRESH_TRUNC) # If pixel value (<150) no change in the image but if pixel values (>150) all values set to 150.
_, th4 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)# If pixel value (<150) all values changed to 0(black) but if pixel values (>150) no change in pixel values
_, th5 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO_INV) #inverse of th4

titles = ['Original','Th_Binary','Th_Binary_INV','Th_TRUNC','Th_TOZERO','Th_TOZERO_INV']
images = [img, th1,th2,th3,th4,th5]

# Using matplotlib
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
#this gives output_1.png

             # OR another method

#cv2.imshow('Image',img)
#cv2.imshow('Th_Binary',th1)
#cv2.imshow('Th_Binary_INV',th2)
#cv2.imshow('Th_TRUNC',th3)
#cv2.imshow('Th_TOZERO',th4)
#cv2.imshow('Th_TOZERO_INV',th5)

# De-allocate any associated memory usage
#cv2.waitKey(0)
#cv2.destroyAllWindows()
