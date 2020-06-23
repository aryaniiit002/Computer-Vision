#Template matching using OpenCV in Python
#Template matching is a technique for finding areas of an image that are similar to a patch (template)

#To find it, the user has to give two input images: Source Image (S) – The image to find the template in and Template Image (T) – 
#The image that is to be found in the source image.

import cv2
import numpy as np

img = cv2.imread('./images/shapes.jpg')
img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

template = cv2.imread('./images/template.png',0)

# Store width and height of template in w and h 
w, h = template.shape[::-1] # -1 to get cols and rows values in reverse order

# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
# Specify a threshold 
threshold = 0.9996
#print(res)

loc = np.where(res >= threshold)

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,0), 2) 

cv2.imshow('Final image',img)
#cv2.imshow('template',template)


cv2.waitKey(0)
cv2.destroyAllWindows()