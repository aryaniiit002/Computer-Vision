# Draw a line segment on image at "Mouse click positions" using OpenCV-Python

import numpy as np
import cv2

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        point.append((x,y))

        if len(point)>=2:
            cv2.line(img,point[-1],point[-2],(255,0,0), 4)
        cv2.imshow('image',img)

# Press Space key to separate the line from the previous point
        if cv2.waitKey(0) ==32:
            point.clear()

img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("image")
point=[]
cv2.setMouseCallback('image',click_event)

while True:
    cv2.imshow("image",img)
    if cv2.waitKey(0)==ord('q'):
        break
cv2.destroyAllWindows
