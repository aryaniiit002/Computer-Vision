# Loading Videos from a Webcam

#Key codes for OpenCV’s cv2.waitKey()

#keycode.KEY_DOWN = 63233
 #   The Arrow Down key
#keycode.KEY_ESCAPE = 27
 #   The ESC key
#keycode.KEY_LEFT = 63234
#    The Arrow Left key
#keycode.KEY_RIGHT = 63235
 #   The Arrow Right key
#keycode.KEY_SPACE = 32
#    The Space key
#keycode.KEY_UP = 63232
#    The Arrow Up key


import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
