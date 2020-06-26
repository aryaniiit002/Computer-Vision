# Circle Detection using OpenCV Hough Circle Transform

import numpy as np
import cv2

img = cv2.imread('caps.png')
output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

#Finds circles in a grayscale image using the Hough transform.
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 30,param1=50, param2=25, minRadius=45, maxRadius=50)
# this give the circle vectors of center coordinates and radius 
# but we need to convert these parameters into an intergers 
detected_circles = np.uint16(np.around(circles))

for (x, y ,r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x, y), 2, (0, 0, 255), 3)

cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()