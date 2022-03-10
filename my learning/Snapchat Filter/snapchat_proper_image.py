

import cv2
import dlib
import numpy as np

from math import hypot

vid = cv2.VideoCapture(0)
pig_image = cv2.imread("nosepick.png")
mushtache_image=cv2.imread("mustache.png")

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

        landmarks=predictor(gray_frame,face)
        # top_nose=(landmarks.part(29).x,landmarks.part(29).y)

        # print(landmarks.part(29).x,landmarks.part(29).y)

        top_nose = (landmarks.part(29).x, landmarks.part(29).y)
        center_nose = (landmarks.part(30).x, landmarks.part(30).y)
        left_nose = (landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)


        # down_nose=(landmarks.part(34).x, landmarks.part(34).y)
        # lip_up2=(landmarks.part(52).x, landmarks.part(52).y)
        # lip_up1=(landmarks.part(51).x, landmarks.part(51).y)
        # lip_up3=(landmarks.part(53).x, landmarks.part(53).y)
        # left_corner_lip=(landmarks.part(49).x, landmarks.part(49).y)
        # right_corner_lip=(landmarks.part(55).x, landmarks.part(55).y)
        
        # mushtache_width=int(right_corner_lip[0]-left_corner_lip[0])
        # mushtache_height=int(lip_up2[0]-down_nose[0])
        # # print("mushtach height",mushtache_height)

        nose_width = int(hypot(left_nose[0] - right_nose[0],
                           left_nose[1] - right_nose[1]) * 1.7)
       
        nose_height = int(nose_width * 0.77)

           # New nose position
        top_left = (int(center_nose[0] - nose_width / 2),
                              int(center_nose[1] - nose_height / 2))

        bottom_right = (int(center_nose[0] + nose_width / 2),
                       int(center_nose[1] + nose_height / 2))
                       # Adding the new nose

        nose_pig = cv2.resize(pig_image, (nose_width, nose_height))
        # mushtache=cv2.resize(mushtache_image,(mushtache_width,mushtache_height))
        # mushtache=cv2.resize(mushtache_image,(100,50))
 
 
        img2gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
        # img_mush_gray= cv2.cvtColor(mushtache,cv2.COLOR_BGR2GRAY)

        ret, nose_mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)
        # ret,mush_mask=cv2.threshold(img_mush_gray, 0, 255, cv2.THRESH_BINARY_INV)

        
        nose_area = frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width]
        
        nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area)
        
        
        # mushtache_area=frame[50:100,50:150]

        # frame [ y-axis, x-axis] 
        # mushtache_area_no_mushtache= cv2.bitwise_and(mushtache_area, mushtache_area)
       
        final_nose = cv2.add(nose_area_no_nose, nose_pig)
        # final_mushtache=cv2.add(mushtache_area_no_mushtache,mushtache)

        # cv2.imshow("mushtach area", final_mushtache)

        frame[top_left[1]: top_left[1] + nose_height,
                    top_left[0]: top_left[0] + nose_width] = final_nose


        # frame[50:100,50:150]=final_mushtache
       
         

        #
        # roi = frame[landmarks.part(29).x:landmarks.part(29).x+100, landmarks.part(29).y:landmarks.part(29).y+100]
        # roi[np.where(mask)] = 0
        # roi += pig_image
	

    cv2.imshow('frame', frame)
      
    if cv2.waitKey(1) == ord('q'):
        break