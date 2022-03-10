import cv2
import dlib
import numpy as np
from math import hypot

vid = cv2.VideoCapture(0)

mushtache_image=cv2.imread("mustache.png")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
  
while(True):
      
    ret, frame = vid.read()
    # frame should be of gray cause requires less cmputational power
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(frame)
    
    for face in faces:

        landmarks=predictor(gray_frame,face)
        # top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y+20)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        # cv2.circle(frame,top_nose,15,(0,0,255),-1) #-1 thickness to fill the circle 
        nose_width = int(hypot(left_nose[0] - right_nose[0],
                           left_nose[1] - right_nose[1]) * 2.5)
       
        nose_height = int(nose_width * 0.5)

           # New nose position
        top_left = (int(center_nose[0] - nose_width / 2),
                              int(center_nose[1] - nose_height / 2))

        bottom_right = (int(center_nose[0] + nose_width / 2),
                       int(center_nose[1] + nose_height / 2))
        # Adding the new nose

        nose_mush = cv2.resize(mushtache_image, (nose_width, nose_height))
        
 
        img2gray = cv2.cvtColor(nose_mush, cv2.COLOR_BGR2GRAY)
        
        _, nose_mask = cv2.threshold(img2gray, 25, 255, cv2.THRESH_BINARY_INV)
        
        
        nose_area = frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width]
        
        nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area,mask=nose_mask)

        final_nose = cv2.add(nose_area_no_nose, nose_mush)
        
        frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width] = final_nose

    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) == ord('q'):
        break