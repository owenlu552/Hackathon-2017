'''
Created on Apr 28, 2017

@author: Owen
'''

import cv2


camera = cv2.VideoCapture(0)
retval, image = camera.read()

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('C:/Users/Owen/Documents/GitHub/opencv/data/haarcascades/haarcascade_frontalface_default.xml')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(gray, 1.3, 5)


print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)