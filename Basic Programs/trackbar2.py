#TrackBar using Trackbar as the Color Palette and changing colored image to grayscale image using Trackbar switch. 
#We can also get get user input with OpenCV trackbars.

import numpy as np
import cv2

def mouse_event(x):
    print(x)

cv2.namedWindow('image')
 
cv2.createTrackbar( "CP", 'image', 10 , 300, mouse_event)

# create switch for color/Grey image functionality
switch = 'color image/Grey image'
cv2.createTrackbar(switch, 'image',0,1,mouse_event)

while (1):
    img = cv2.imread('./images/cards.png')

    pos = cv2.getTrackbarPos('CP' , 'image')
    font= cv2.FONT_HERSHEY_SIMPLEX

    #to put position of trackbar scrolled by user on image
    cv2.putText(img,str(pos),(50,100), font, 1,(0,0,255), 3, cv2.LINE_AA)
    k = cv2.waitKey(1) & 0xFF
    if k ==32:
        break

    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    img = cv2.imshow('image',img)

cv2.destroyAllWindows()