# This programs smoothens an image using the various filters

import numpy
import cv2

img = cv2.imread("./img_videos/flower.png")
#img=cv2.resize(img,(512,512))

noisereduced_version=cv2.medianBlur(img,9)   # ksize[, dst]) should be any Odd number
Bilateral= cv2.bilateralFilter(img,15,50,75)
average_filter = cv2.blur(img,(5,5))
Gaussian_Image= cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("original_image",img)
cv2.imshow("Median Blur",noisereduced_version)
cv2.imshow("Bilateral Image",Bilateral)
cv2.imshow("average filter",average_filter)
cv2.imshow("Gaussian_Image",Gaussian_Image)


cv2.waitKey(0)


#The higher the kernel value, the lower the noise and the higher the blur.
#When you run the program you will find it is easy to note that all these denoising filters smudges the edges, 
#while bilateral retains them.

#Check this link give below for more information about filters
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
