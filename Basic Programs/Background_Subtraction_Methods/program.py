#Background Subtraction in live video using Concept of Running Average -

#Background subtraction is a technique for separating out foreground elements from the background
#and is done by generating a foreground mask.
#This technique is used for detecting dynamically moving objects from static cameras. 
#Background subtraction technique is important for object tracking.

import cv2 
import numpy as np 
  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
  
# read the frames from the camera 
_, img = cap.read() 
  
# modify the data type setting to 32-bit floating point 
averageValue1 = np.float32(img)

while(1): 
    # reads frames from a camera  
    _, img = cap.read() 
      
    # using the cv2.accumulateWeighted() function that updates the running average 
    cv2.accumulateWeighted(img, averageValue1, 0.02) 
      
    # converting the matrix elements to absolute values and converting the result to 8-bit.  
    resultingFrames1 = cv2.convertScaleAbs(averageValue1) 
  
    # Show two output windows the input / original frames window 
    cv2.imshow('InputWindow', img) 
  
    # the window showing output of alpha value 0.02 
    cv2.imshow('averageValue1', resultingFrames1) 
       
    k = cv2.waitKey(30) & 0xff
    if k == 32:  
        break
  
# Close the window  
cap.release()  
    
# De-allocate any associated memory usage  
cv2.destroyAllWindows() 
