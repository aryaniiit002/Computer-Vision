#Morphological Transformations ->
#Morphological transformations are some simple operations based on the image shape. 
#It is normally performed on binary images.
# https://docs.opencv.org/trunk/d9/d61/tutorial_py_morphological_ops.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY) 

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(mask,kernel,iterations = 3)
dilation = cv2.dilate(mask, kernel, iterations=3)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)#Opening is just another name of erosion followed by dilation.
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #Closing is reverse of Opening, Dilation followed by Erosion
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)


titles = ['image','mask', 'dilation', 'erosion', 'opening','closing','gradient']
images = [img,mask, dilation, erosion, opening, closing, gradient]
for i in range(7):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()