#Mean Shift Object Tracking - 

#Meanshift is a very useful method to keep track of a particular object inside a video.
#Meanshift can separate the static background of a video and the moving foreground object.
# Read the theory: https://www.geeksforgeeks.org/python-opencv-meanshift/

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

#Iterate through each frame, calculate the histogram back projection,
#apply the meanshift method to get the new location and draw it on the
#window, and iterate until the condition terminates.
while(1):
    ret, frame = cap.read()
    if ret == True:

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Calculate the histogram back projection
        # Each pixel's value is it's probability
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
#the function computes probability of each element value in respect 
#with the empirical probability distribution represented by the histogram

        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        final_image = cv.rectangle(frame, (x,y), (x+w, y+h), 255, 3)

       # cv.imshow('dst', dst)
        cv.imshow('final_image',final_image)

        k = cv.waitKey(30) & 0xff
        if k == 32:
            break
    else:
        break