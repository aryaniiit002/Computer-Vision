# Optical Flow with Lucas-Kanade method – Using **Mouse callBack Function**

#Program uses mouse callBack function that helps the user to track any object any time he wants to.

import cv2
import numpy as np

def mouse_callback(event,x,y,flags, params):
    global point, point_selected,old_points

    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x,y)
        point_selected = True
        old_points = np.array([[x, y]], dtype=np.float32)

point_selected = False
point = ()

# Lucas kanade params
lucas_kanade_params = dict(winSize = (25, 25),
maxLevel = 2,criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse_callback)

cap = cv2.VideoCapture('test_video.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Mouse_callBack_output_video.avi',fourcc, 40.0,(int(cap.get(3)),int(cap.get(4))))

#create old_frame
_ , old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame,cv2.COLOR_BGR2GRAY)

old_points = np.array([[]])

while (1):
    _, frame = cap.read()

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    if point_selected is True: 
        cv2.circle(frame, point, 5, (0, 0, 255), 2)

        new_points, status, error = cv2.calcOpticalFlowPyrLK(old_gray, gray_frame, old_points, None, **lucas_kanade_params)
        
        old_gray = gray_frame.copy()
        old_points = new_points
        x, y = new_points.ravel() 
        
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
    
    cv2.imshow("Frame",frame)
    out.write(frame)

    if cv2.waitKey(25)==32:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
    