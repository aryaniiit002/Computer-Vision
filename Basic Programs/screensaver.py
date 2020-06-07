# Creating a Bouncing Ball Screensaver using OpenCV-Python
# Task- Create a Window that we can write text on. If we don’t write for 5 seconds screensaver will start.

import cv2
import numpy as np

def screensaver():
    img = np.zeros((480,640,3),dtype='uint8')
    dx,dy =1,1
    x,y = 100,100
    while True:
        # Display the image
        cv2.imshow('Screensaver',img)
        k = cv2.waitKey(10)
        img = np.zeros((480,640,3),dtype='uint8')  #This line will help in making different circle everytime loop runs.
        # Increment the position
        x = x+dx
        y = y+dy
        cv2.circle(img,(x,y),20,(255,130,140),-1)
        if k != -1:
            break
        # Change the sign of increment on collision with the boundary
        if y >=480 or y<=0 :
           dy *= -1

        if x >=640 or x<=0 :
           dx *= -1
    cv2.destroyAllWindows()

# Background Image
img1 = cv2.imread('./images/aryan__bindal.jpg')
# Initialize these for text placement
i = 0 
a,b = 30,30
while True:
    cv2.imshow('My Photo',img1)
    k = cv2.waitKey(5000)
    # If no key is pressed, display the screensaver
    if k == -1:
        screensaver()
    # Press q to quit
    elif k == ord('q'):
        break
    # Otherwise write real time text on the image.
    # This is used for visualization only
    # You can use anything here.
    else:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,chr(k),(a+i,b), font, 1,(0,0,0),3,cv2.LINE_AA)
 # The shape[] attribute for numpy arrays returns the dimensions of the array. If Y has n rows and m columns, then Y.shape is (n,m).
 # So Y.shape[0] is n and Y.shape[1] is m.
        if a+i >= img1.shape[1]:
            b = b+15
            i = 0
        i +=20
        
cv2.destroyAllWindows()
