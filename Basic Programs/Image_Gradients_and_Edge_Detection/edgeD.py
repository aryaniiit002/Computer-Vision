# Image Gradients and Edge Detection

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sudoku_.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Compute the Laplacian of the image -
#We use a 64bit float due to the negative slope induced by transforming the image from white-to-black. 
#{Black-to-White transition is taken as Positive slope while White-to-Black transition as Negative slope}
#So when you convert data to np.uint8, all negative slopes are made zero. In simple words, you miss some edges.
#If you want to detect all edges, better option is to keep the output datatype to some higher forms, like cv2.CV_16S, cv2.CV_64F etc, 
#take its absolute value and then convert back to cv2.CV_8U or np.uint8
#A 64bit float supports the negative numbers we’ll be dealing with when the Laplacian method is run

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))  #convert to unsigned 8 bit interger

# Compute gradients along the X and Y axis, respectively
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

# The sobelX and sobelY images are now of the floating point data type -- we need to take care when converting
# back to an 8-bit unsigned integer that we do not miss any images due to clipping values outside the range
# of [0, 255]. First, we take the absolute value of the gradient magnitude images, THEN we convert them back
# to 8-bit unsigned integers
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

#to combine the result of sobelx and sobely
sobelCombined = cv2.bitwise_or(sobelx , sobely)

canny = cv2.Canny(img, 10, 255) # manage the threshold1[min] and threshold2[max] for best result

titles = ['original img', 'laplacian','sobelx','sobely','sobelCombined','canny Image']
images = [img, lap, sobelx,sobely,sobelCombined, canny]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html