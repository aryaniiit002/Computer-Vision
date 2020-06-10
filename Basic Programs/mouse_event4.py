# Create a window filled with the same color as the point on image at "Mouse click position"

import cv2
import numpy as np

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:

        blue= img[y,x,0]
        green= img[y,x,1]
        red= img[y,x,2]

        cv2.circle(img, (x,y), 4, (0,0,255), -1)

        output_img=np.zeros((512,512,3),np.uint8)
        output_img[:] = [blue,green,red]

        cv2.imshow('O/P_image',output_img)


img=cv2.imread('./img_videos/mypic2.jpg')
img= cv2.resize(img, (600,600))

cv2.imshow('Image',img)

cv2.setMouseCallback('Image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows