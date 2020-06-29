#Object Tracking Camshift Method - CAMshift (Continuously Adaptive Meanshift)

#With the help of Camshift algorithm, the size of the window keeps updating when the tracking window tries to converge. 
#Read here: https://www.geeksforgeeks.org/track-objects-with-camshift-using-opencv/

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('slow_traffic_small.mp4')

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 300, 192, 100, 50
track_window = (x, y ,width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x : x+width]

hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# Create a mask between the HSV bounds
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))

# Obtain the color histogram of the ROI
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv.normalize(roi_hist, roi_hist, 0, 255,cv.NORM_MINMAX) 
#min value of dst is alpha and max value of dst is beta

# Setup the termination criteria either can be a fixed set of ten
#iterations or can be set to when the centroid is shifted by at least one pixel
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 20, 1)

cv.imshow('roi',roi)

while(1):
    ret, frame = cap.read()
    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # apply CamShift to get the new location
        ret, track_window = cv.CamShift(dst, track_window, term_crit)

        # Draw it on image -

        pts = cv.boxPoints(ret)
        #Finds the four vertices of a rotated rect. Useful to draw the rotated rectangle.

        #print(pts)
        pts = np.int0(pts)
        
        final_image = cv.polylines(frame, [pts], True, (0, 255, 0), 2)
       
        cv.imshow('dst', dst)
        cv.imshow('final_image',final_image)

        k = cv.waitKey(30) & 0xff
        if k == 32:
            break
    else:
        break
