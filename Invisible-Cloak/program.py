#Invisibility Cloak using Color Detection and Segmentation with OpenCV

import cv2 
import numpy as np 
import time 
 
cap_video = cv2.VideoCapture(0) 
     
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi',fourcc, 10.0,(int(cap_video.get(3)),int(cap_video.get(4))))

# give the camera to warm up 
time.sleep(1)  
rate = 0 
background = 0 
  
# capturing the background in range of 60 you should have video that have some seconds 
# dedicated to background frame so that it could easily save the background image 
for i in range(60): 
    ret, background = cap_video.read() 
    if ret == False : 
        continue 
  
background = np.flip(background, axis = 1) # flipping of the frame  
  
# we are reading from video  
while (cap_video.isOpened()): 
    return_val, img = cap_video.read() 
    if not return_val : 
        break 
    rate = rate + 1
    img = np.flip(img, axis = 1) 
  
    # convert the image - BGR to HSV as we focused on detection of red color  
    # converting BGR to HSV for better detection or you can convert it to gray 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

    # Range for lower red
    lower_red = np.array([0,120,70])        
    upper_red = np.array([10,255,255]) 
    mask1 = cv2.inRange(hsv, lower_red, upper_red) 

    # range for Upper Red 
    lower_red = np.array([155, 40, 40]) 
    upper_red = np.array([180,255,255]) 
    mask2 = cv2.inRange(hsv, lower_red, upper_red) 

    # the above block of code could be replaced with some other code depending upon the color of your cloth  
    mask1 = mask1 + mask2 
  
    # Refining the mask corresponding to the detected red color 
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) 
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8)) 
    mask2 = cv2.bitwise_not(mask1) 
  
    # Generating the final output 
    result1 = cv2.bitwise_and(background, background, mask = mask1) 
    result2 = cv2.bitwise_and(img, img, mask = mask2) 
    output = cv2.addWeighted(result1, 1, result2, 1, 0) 
    out.write(output)
    cv2.imshow("INVISIBLE CLOAK", output) 

    key = cv2.waitKey(10) 
    if key == 32: 
        break
out.release()
