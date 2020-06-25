# Road Lane Line Detection in an Image - with OpenCV

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Now we define a function that will mask every other thing than our region of interest

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  #blank matrix that matches the img height and width
    #channel_count = img.shape[2]  #retrive the number of color channels in img
    match_mask_color = 255  #create a match color with same color channel_count
    cv2.fillPoly(mask, vertices, match_mask_color) #Fills the area bounded by one or more polygons.
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

#Region of Interest: This step is to take into account only the region covered by the road lane.
# A mask is created here, which is of the same dimension as our road image. 
# Furthermore, bitwise AND operation is performed between each pixel of our img and this mask. 
# It ultimately masks the img and shows the region of interest traced by the region_of_interest_vertices contour of the mask.

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (255, 0, 0), thickness=6)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

image = cv2.imread('lane1.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#print(image.shape)    #(height,width,channels)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2 , height/2 -10),
    (width, 256)
]

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_image, (3, 3), 0) 
canny_image = cv2.Canny(blur, 55, 192)

cropped_image = region_of_interest(canny_image,np.array([region_of_interest_vertices], np.int32),)

lines = cv2.HoughLinesP(cropped_image,
                        rho=3,
                        theta=np.pi/180,
                        threshold=100,
                        lines=np.array([]),
                        minLineLength=0,
                        maxLineGap=8)
image_with_lines = draw_the_lines(image, lines)


titles = ['original image','canny_image','cropped_image','image_with_lines']
images = [image,canny_image, cropped_image,image_with_lines]

for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()