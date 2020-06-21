# Image Pyramids with Python and OpenCV

#Normally, we work with images with default resolution but many times we need to change the resolution (lower it) or resize the original image in that case image pyramids comes handy.
#The pyrUp() function increases the size to double of its original size and pyrDown() function decreases the size to half. 
#If we keep the original image as a base image and go on applying pyrDown function on it and keep the images in a vertical stack
#, it will look like a pyramid. 
#The same is true for upscaling the original image by pyrUp function.

import cv2
import numpy as np

img = cv2.imread('panda.jpg')

#There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
#1st Gaussian Pyramid -
#lr = cv2.pyrDown(img)   #area reduces to 1/4 of original area
#lr2= cv2.pyrDown(lr)    #area reduces to 1/8 of original area

#hr = cv2.pyrUp(lr2)
#hr2 = cv2.pyrUp(hr)

#cv2.imshow('Image',img)
#cv2.imshow('pyrDown1',lr)
#cv2.imshow('pyrDown2',lr2)
#cv2.imshow('pyrUp1',hr)
#cv2.imshow('pyrUp2',hr2)

#Once we scale down and if we rescale it to the original size, 
#we lose some information and the resolution of the new image is much lower than the original one.

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Advantages of Image pyramids:
    #Lowering of resolution
    #Getting various sizes of image
    #Image Blending
    #Edge detection  "Laplacian pyramid images are like edge images only. Most of its elements are zeros".
                             #OR

duplicate = img.copy()
arr_gp = [duplicate]

for i in range(3):
    duplicate= cv2.pyrDown(duplicate)
    arr_gp.append(duplicate)
    #cv2.imshow(str(i),duplicate)

#2nd Laplacian Pyramids - 
#Laplacian Pyramids are formed from the Gaussian Pyramids.
# A level in Laplacian Pyramid is formed by the difference between 
#that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid. (Read that again)

for i in range(2,0,-1):
    extended_duplicate = cv2.pyrUp(arr_gp[i])
    laplacian = cv2.subtract(arr_gp[i-1],extended_duplicate) 
    cv2.imshow(str(i-1),laplacian)  #Laplacian pyramid images
    
cv2.waitKey(0)
cv2.destroyAllWindows()                

#we will see Image Blending in other programs 
#check out img_blending.py