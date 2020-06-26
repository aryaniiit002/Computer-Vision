#Face Detection using Haar Cascade Classifiers

import cv2

#will use pretrained Haar cascade models to detect faces and eyes in an image or in video.
#Download the xml file from here:  https://github.com/opencv/opencv/tree/master/data/haarcascades 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
#img = cv2.imread('mypic2.jpg')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10) 
    # returns boundary rectangles params for the detected faces or eyes.

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0 , 255), 3)

    # Display the output
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == 32:
        break

cap.release()