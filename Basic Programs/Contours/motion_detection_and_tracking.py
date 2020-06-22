#  Motion Detection and Tracking Using OpenCV Contours

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#out = cv2.VideoWriter("output_video.mp4v", fourcc, 10, (1280,720))

ret , frame1 = cam.read()
ret , frame2 = cam.read()
while cam.isOpened():
    diff = cv2.absdiff(frame1, frame2) #calculate the absolute differene btw 1st and the 2nd frame
    # Converting color diff image to gray_scale image 
    gray = cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)
    # Converting gray scale image to GaussianBlur so that change can be find easily 
    blur = cv2.GaussianBlur(gray, (5, 5), 0) 
    _ , thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    # Finding contour of moving object 
    contours, _ = cv2.findContours(dilated , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 1500:  #if area of contour is <900 no rectangle will be drawn
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)


    #image = cv2.resize(frame1, (1280,720))
    #out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret ,frame2 =cam.read()

    if cv2.waitKey(10) ==32 :
        break

cam.release()
cv2.destroyAllWindows()
#out.release()