# Dense Optical Flow Algorithm -

#Colors are used to reflect movement, with the hue representing the direction and the
#value representing the speed. This makes this algorithm relatively slower.

#First, load the input video and get the hue colors for the first frame. 
# For each frame, convert it to grayscale, compute the optical flow, and calculate
#the magnitude and the color to reflect the speed of the angle, mark the
#color in the frame, and show the video until the frames are exhausted.

import cv2
import numpy as np

# Get a VideoCapture object from video and store it in vs
vc = cv2.VideoCapture("test_video.mp4")

# Read first frame
ret, first_frame = vc.read()

# Scale and resize image
resize_dim = 600
max_dim = max(first_frame.shape)

scale = resize_dim/max_dim

first_frame = cv2.resize(first_frame, None, fx=scale, fy=scale)

# Convert to gray scale 
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

# Create mask
mask = np.zeros_like(first_frame)

## Set image saturation to maximum value as we do not need it
mask[..., 1] = 255

#out = cv2.VideoWriter('video.mp4',-1,1,(600, 600))

while(vc.isOpened()):
    # Read a frame from video
    ret, frame = vc.read()
    
    # Convert new frame format`s to gray scale and resize gray frame obtained
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=scale, fy=scale)

    # Computes the dense optical flow using the Gunnar Farneback’s algorithm
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, pyr_scale = 0.5, levels = 5, winsize = 11, iterations = 5, poly_n = 5, poly_sigma = 1.1, flags = 0)
   
    # Compute the magnitude and angle of the 2D vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
   
    # Set image hue according to the optical flow direction
    mask[..., 0] = angle * 180 / np.pi / 2
   
    # Set image value according to the optical flow magnitude (normalized)
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    
    # Convert HSV to RGB (BGR) color representation
    rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    
    # Resize frame size to match dimensions
    frame = cv2.resize(frame, None, fx=scale, fy=scale)
    
    # Open a new window and displays the output frame
    dense_flow = cv2.addWeighted(frame, 1,rgb, 2, 0)
    
    cv2.imshow("Dense optical flow", dense_flow)
    #out.write(dense_flow)
    
    # Update previous frame
    prev_gray = gray
    
    k = cv2.waitKey(30)
    if k ==32:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.png',frame)
        cv2.imwrite('opticalhsv.png',dense_flow)

# The following frees up resources and closes all windows
vc.release()
cv2.destroyAllWindows()
