# Canny Edge detection

import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('image')

# When performing Canny edge detection we need two values for hysteresis: threshold1 and threshold2. Any gradient
# value larger than threshold2 are considered to be an edge. Any value below threshold1 are considered not to
# ben an edge. Values in between threshold1 and threshold2 are either classified as edges or non-edges based on how
# the intensities are "connected".
cv2.createTrackbar("threshold1",'image',0,255,nothing )
cv2.createTrackbar("threshold2",'image',255,255, nothing )

while (1):
    img = cv2.imread('cards.png', cv2.IMREAD_GRAYSCALE)

    k = cv2.waitKey(1) & 0xFF
    if k ==32:
        break

    th1 = cv2.getTrackbarPos('threshold1','image')
    th2 = cv2.getTrackbarPos('threshold2','image')

    canny = cv2.Canny(img, th1, th2)

    cv2.imshow('original image',img)
    cv2.imshow('canny Image',canny)


cv2.destroyAllWindows()