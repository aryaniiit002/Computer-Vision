#Object Detection and Object Tracking Using HSV Color Space
#we will be Implementing color and shape-based object detection and tracking using  hue-saturation-value (HSV) color model. 
#For Choosing the correct upper and lower HSV boundaries for color detection with`cv::inRange` (OpenCV) we will use trackbar.


import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow("tracking")
frame = cv2.imread('./images/smarties.png')
frame = cv2.resize(frame, (240,240))

#we will create Trackbars to make the output more clear and dynamic
cv2.createTrackbar("LH", 'tracking', 0, 255, nothing)
cv2.createTrackbar("LS", 'tracking', 0, 255, nothing)
cv2.createTrackbar("LV", 'tracking', 0, 255, nothing)
cv2.createTrackbar("UH", 'tracking', 255, 255, nothing)
cv2.createTrackbar("US", 'tracking', 255, 255, nothing)
cv2.createTrackbar("UV", 'tracking', 255, 255, nothing)


while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h= cv2.getTrackbarPos('LH', 'tracking')
    l_s= cv2.getTrackbarPos('LS', 'tracking') 
    l_v= cv2.getTrackbarPos('LV', 'tracking')
    u_h= cv2.getTrackbarPos('UH', 'tracking')
    u_s= cv2.getTrackbarPos('US', 'tracking')
    u_v= cv2.getTrackbarPos('UV', 'tracking')

    l_b = np.array([l_h, l_s, l_v])
    h_b = np.array([u_h, u_s, u_v])

#Whichever region in the image you want to process,
#those region in mask should be white, everything else is black
    mask = cv2.inRange(hsv, l_b, h_b)

    result = cv2.bitwise_and(frame,frame, mask= mask)
#What happened is, the spatial locations where the mask had a pixel value zero (black), 
#became pixel value zero in the result image.
#The locations where the mask had pixel value 255 (white), the resulting image retained it's original value.

    cv2.imshow('Original',frame)
    #cv2.imshow('hsv',hsv)
    cv2.imshow('result',result)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 32:
       break

cv2.destroyAllWindows()
