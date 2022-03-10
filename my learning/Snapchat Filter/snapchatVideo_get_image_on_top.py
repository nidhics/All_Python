

import cv2
import dlib
import numpy as np

from math import hypot

vid = cv2.VideoCapture(0)
pig_image = cv2.imread("nosepick.png")

# logo = cv2.imread('nosepick.png')
size = 20
pig_image = cv2.resize(pig_image, (size, size))



      

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
  
while(True):
      
    ret, frame = vid.read()
    # frame should be of gray cause requires less cmputational power
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    # roi += pig_image
    
    faces = detector(frame)
    
    for face in faces:
        # print(face)

        img2gray = cv2.cvtColor(pig_image, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)

        landmarks=predictor(gray_frame,face)
        top_nose=(landmarks.part(29).x,landmarks.part(29).y)

        print(landmarks.part(29).x,landmarks.part(29).y)
       
       
        size = 20
        pig_image = cv2.resize(pig_image, (size, size))
        roi=frame[0:20,0:20]
       
        # roi = frame[landmarks.part(29).x:landmarks.part(29).x+100, landmarks.part(29).y:landmarks.part(29).y+100]
        roi[np.where(mask)] = 0
        roi += pig_image
	
        cv2.circle(frame,top_nose,15,(0,0,255),-1) #-1 thickness to fill the circle 
       
 
        # nose_area=frame[:]
        # cv2.imshow("nose top",pig_image)


    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) == ord('q'):
        break