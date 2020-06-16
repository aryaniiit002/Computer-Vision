# This function (cv2.medianBlur(src, ksize[, dst])) smoothens an image using the median filter
# ksize[, dst]) should be any Odd number

import numpy
import cv2

img = cv2.imread("./img_videos/flower.png")
#img=cv2.resize(img,(512,512))

noisereduced_version=cv2.medianBlur(img,9)
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
# It is easy to note that all these denoising filters smudges the edges, while bilateral retains them.