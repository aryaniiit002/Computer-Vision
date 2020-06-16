#Here we will create a simple application which shows the color you specify.
#You have a window which shows the color and three trackbars to specify each of B,G,R colors.
#You slide the trackbar and correspondingly window color changes.
#By default, initial color will be set to Black.

import numpy as np
import cv2

def mouse_event(x):
    print(x)

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
#img[:] = [255,255,255]
#img = cv2.imread('./images/name.jpg')
cv2.namedWindow('image')
 
# create trackbars for color change
cv2.createTrackbar( "B", 'image', 0 , 255, mouse_event)
cv2.createTrackbar( "G", 'image', 0 , 255, mouse_event)
cv2.createTrackbar( "R", 'image', 0 , 255, mouse_event)
#We can also create one switch in which application works only if switch is ON, otherwise screen is always black.
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,mouse_event)


while (1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 32:
        break

    # get current positions of four trackbars
    b = cv2.getTrackbarPos('B' , 'image')
    g = cv2.getTrackbarPos('G' , 'image')
    r = cv2.getTrackbarPos('R' , 'image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
