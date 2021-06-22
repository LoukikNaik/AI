import cv2
from random import randrange
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#img=cv2.imread('Fest.jpeg')
webcam=cv2.VideoCapture(0)
while True:
    successful_frame_read,frame=webcam.read()
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for i in range(len(face_coordinates)):
        (x,y,w,h)=face_coordinates[i]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('Face Detector',frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break
webcam.release()
"""
FOR IMAGES
grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
print(face_coordinates)
for i in range(len(face_coordinates)):
    (x,y,w,h)=face_coordinates[i]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow('Face Detector',img)
cv2.waitKey()"""

print("Code Completed")