# Optical Flow with Lucas-Kanade method –

#The Lucas–Kanade differential algorithm helps in tracking the keypoints of an object in a video
# that has corner features such as tracking a car on the race track (by a drone).

import numpy as np 
import cv2 

cap = cv2.VideoCapture('test_video.mp4') 

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output_video.avi',fourcc, 40.0,(int(cap.get(3)),int(cap.get(4))))

# params for corner detection 
feature_params = dict( maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7 ) 

# Parameters for lucas kanade optical flow 
lk_params = dict( winSize = (10, 10), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 

# Create some random colors 
color = np.random.randint(0, 255, (100, 3)) 

# Take first frame and find corners in it 
ret, old_frame = cap.read() 
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY) 
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params) 

# Create a mask image for drawing purposes 
mask = np.zeros_like(old_frame) 

while(1): 
	
	ret, frame = cap.read() 
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

	# calculate optical flow 
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params) 

	# Select good points 
	good_new = p1[st == 1] 
	good_old = p0[st == 1] 

	# draw the tracks 
	for i, (new, old) in enumerate(zip(good_new, good_old)): 
		a, b = new.ravel() 
		c, d = old.ravel() 
		mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2) 
		frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
         
	#cv2.imshow('mask', mask) 
	img = cv2.add(frame, mask) 

	cv2.imshow('frame', img) 
	#out.write(img)
	k = cv2.waitKey(25) 
	if k == 32: 
		break

	# Updating Previous frame and points 
	old_gray = frame_gray.copy() 
	p0 = good_new.reshape(-1, 1, 2) 

	

#out.release()
cap.release() 
cv2.destroyAllWindows() 