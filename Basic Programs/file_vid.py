# Loading Videos from a File

import cv2
import numpy as np

video = cv2.VideoCapture("Legends Never Die.mp4")
while True:
    ret, frame = video.read()

    cv2.imshow("frame", frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()