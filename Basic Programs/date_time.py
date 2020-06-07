# Show current Date and time on live video using OpenCV-Python

    # Open the camera using cv2.VideoCapture()
    # Until the camera is open
    #    Grab each frame using cap.read()
    #    Put the current DateTime on each frame using cv2.putText().
    #    Display each frame using cv2.imshow()
    # On termination, release the webcam and destroy all windows using cap.release() and cv2.destroyAllWindows() respectively.

import cv2
from datetime import datetime
# Open the Camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Put current DateTime on each frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    # Display the image
    cv2.imshow('webcam',frame)
    # wait for keypress
    k = cv2.waitKey(10)
    if k == 32:     #space Key
        break
cap.release()
cv2.destroyAllWindows()