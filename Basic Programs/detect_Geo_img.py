#Detect Simple Geometric Shapes using OpenCV in Python

import cv2
import numpy as np

img = cv2.imread('./images/shapes4.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(imgGray, 199,255,cv2.THRESH_BINARY)
contours , _ =cv2.findContours(thresh , cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (10, 110,255), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]-5

    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))
    
    elif len(approx) == 6:
        cv2.putText(img, "Hexagone", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))

    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        #print(aspectRatio)
       
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "square", (int(x), y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))
    
        else:
          cv2.putText(img, "rectangle", (int(x), y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))
    
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))
    
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))
    
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 110))

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()