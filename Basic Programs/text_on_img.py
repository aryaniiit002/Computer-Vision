# Write Text on images
# cv2.putText(img, text, position, font, fontScale, color, thickness, lineType, bottomLeftOrigin)-- line16

import numpy
import cv2

# Read the image
img = cv2.imread('./images/panda.jpg')

# initialize counter
i = 0
while True:

    # Display the image
    cv2.imshow('a',img)

    # wait for keypress
    k = cv2.waitKey(0)

    # specify the font and draw the key using puttext
    font = cv2.FONT_HERSHEY_SIMPLEX

# cv2.putText(img, text, position, font, fontScale, color, thickness, lineType, bottomLeftOrigin)
# ord(‘q’) converts the character to an int while chr(113) does exactly the opposite i.e. to 'q'

    cv2.putText(img,chr(k),(140+i,250), font, 1,(250,200,120),3,cv2.LINE_AA)

    i+=20

    if k == ord('q'):
        break

cv2.destroyAllWindows()