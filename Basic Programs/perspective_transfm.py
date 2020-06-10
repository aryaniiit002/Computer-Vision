# OpenCV PerspectiveTransform Example

import numpy as np
import cv2

img=cv2.imread('./img_videos/cards.png')
width , height= 350, 200

ptn1=np.float32([[72,124],[72,320],[351,124],[351,320]])
ptn2=np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix= cv2.getPerspectiveTransform(ptn1,ptn2)
req_img=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original image",img)
cv2.imshow('Output Image', req_img)
cv2.waitKey(0)