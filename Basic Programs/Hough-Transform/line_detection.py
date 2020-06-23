#Hough Line Transform using HoughLines method in OpenCV

#Hough Transform is a popular technique to detect any shape, 
# if you can represent that shape in mathematical form. 
# It can detect the shape even if it is broken or distorted a little bit. 

import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar("threshold1",'image',132,255,nothing )
cv2.createTrackbar("threshold2",'image',255,255, nothing )
cv2.createTrackbar("votes",'image',190,255, nothing )

while (1):
    img = cv2.imread('lane2.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    k = cv2.waitKey(1) & 0xFF
    if k ==32:
        break

    th1 = cv2.getTrackbarPos('threshold1','image')
    th2 = cv2.getTrackbarPos('threshold2','image')
    th3 = cv2.getTrackbarPos('votes','image')

    edges = cv2.Canny(gray, th1, th2, apertureSize=3)

    cv2.imshow('original image',img)
    #cv2.imshow('canny Image',edges)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, th3)
#It simply returns an array of (\rho, \theta) values.\rho is measured in pixels and \theta is measured in radians

#adjust TrackBars for better result 

    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)

        #(Xo,Yo) is origin i.e, top left corner 
        x0 = a * rho
        y0 = b * rho      

    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
        x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
        y1 = int(y0 + 1000 * (a))

    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
        x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imshow('Final image', img)   
      
k = cv2.waitKey(0)
cv2.destroyAllWindows()