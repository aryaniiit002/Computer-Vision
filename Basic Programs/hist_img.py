#Working with a Histogram Representation

import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("./images/panda.jpg")
histogram_image = cv2.calcHist([image], [0], None, [256],[0,256])
plt.hist(histogram_image.ravel(), 256, [0,256])
plt.show()

color = ['b','g','r']

for i,col in enumerate(color):
    hist=cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
plt.show()