# Loading Videos from a File

import cv2
import numpy as np

video = cv2.VideoCapture("Legends Never Die.mp4")
if not video.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    ret, frame = video.read()
    # if frame is read correctly ret is True
     if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break

    cv2.imshow("Legends Never Die", frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
