import numpy as np
import cv2

def mouse_event(x):
    print(x)


img = np.zeros((300,512,3), np.uint8)
img[:] = [255,255,255]
#img = cv2.imread('./images/name.jpg')
cv2.namedWindow('image')
 
cv2.createTrackbar( "B", 'image', 0 , 255, mouse_event)
cv2.createTrackbar( "G", 'image', 0 , 255, mouse_event)
cv2.createTrackbar( "R", 'image', 0 , 255, mouse_event)


while (1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k ==32:
        break

    b = cv2.getTrackbarPos('B' , 'image')
    g = cv2.getTrackbarPos('G' , 'image')
    r = cv2.getTrackbarPos('R' , 'image')

    img[:] = [b, g, r]

cv2.destroyAllWindows()