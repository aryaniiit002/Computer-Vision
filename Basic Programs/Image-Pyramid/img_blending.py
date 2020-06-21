#  Image Blending using Pyramids in OpenCV

#One application of Pyramids is Image Blending. 
#For example, in image stitching, you will need to stack two images together, 
#but it may not look good due to discontinuities between images. 
#In that case, image blending with Pyramids gives you seamless blending without leaving much data in the images.

#steps -
#   1)  Load the two images of apple and orange
#   2)  Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
#   3)  From Gaussian Pyramids, find their Laplacian Pyramids
#   4)  Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
#   5)  Finally from this joint image pyramids, reconstruct the original image.

import cv2
import numpy as np

apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')
apple = cv2.resize(apple,(512,512))
orange = cv2.resize(orange,(512,512))

#Image Blending method no. 1

apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
cv2.imshow('apple_orange',apple_orange)  #Not that good so...

#Image Blending method no. 2

# generate Gaussian pyramid for Apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Laplacian Pyramid for Apple
lp_apple = [gp_apple[5]]         
for i in range(5,0,-1):
    extnd_apple = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],extnd_apple)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
lp_orange = [gp_orange[5]]
for i in range(5,0,-1):
    extnd_orange = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],extnd_orange)
    lp_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# now reconstruct by adding the gaussian and laplacian images of same level
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)   # gives colored image
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("Final image",apple_orange_reconstruct)

cv2.imwrite("Final image.jpg",apple_orange_reconstruct)
cv2.imwrite("apple_orange.jpg",apple_orange)

cv2.waitKey(0)
cv2.destroyAllWindows()