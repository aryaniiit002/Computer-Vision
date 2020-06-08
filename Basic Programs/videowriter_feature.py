# Reading the Video and Writing into a File

#The same code is used to read the video and write to a file, except when
#each frame is read, a new parameter holds the read frame in a flip mode
#and writes the flipped frame into another video file.

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.mp4v', fourcc, 10, (1280,720))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret: 
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = cv.flip(frame, 1)
    
    # write the flipped frame
    out.write(frame)
    
    cv.imshow('Video',frame)
    
    if cv.waitKey(1) == 32:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
