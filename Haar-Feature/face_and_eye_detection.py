#  Face and Eye Detection Haar Feature based Cascade Classifiers

#will use pretrained Haar cascade models to detect faces and eyes in an image or in video.
#Download the xml file from here:  https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 3)

    # Display the output
    cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == 32:
        break

cap.release()