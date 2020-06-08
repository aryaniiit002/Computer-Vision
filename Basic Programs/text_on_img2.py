# Write Text on images at "Mouse click position" using OpenCV-Python

#steps -     Create a mouse callback function where on every left double click position we put text on the image.
             # Create or read an image.
             # Create an image window using cv2.namedWindow()
             # Bind the mouse callback function to the image window using cv2.setMouseCallback()
             # Display the new image using an infinite while loop

import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        i = 0
        while True:
            cv2.imshow('image',img) # to display the characters
            k = cv2.waitKey(0)
            cv2.putText(img, chr(k) , (x+i,y), font, 1, (0, 255, 0),3, cv2.LINE_AA)
            i+=20

            # Press q to stop writing
            if k == ord('q'):
                break

    

# Create a white image, a window and bind the function to window
img = np.ones((720,720))

# The function namedWindow just makes sure that if you wish to do something with that same window afterwards 
# (eg move, resize, close that window), you can do it by referencing it with the same name
cv2.namedWindow('image')

# Bind the mouse callback function to the image window using cv2.setMouseCallback()
cv2.setMouseCallback('image',draw_circle)

# Display the new image using an infinite while loop
while True:
    cv2.imshow('image',img)
    if cv2.waitKey(20) == 32:
        break
cv2.destroyAllWindows()

# In the above code, press ‘q’ to stop writing and left double click anywhere to again start writing.