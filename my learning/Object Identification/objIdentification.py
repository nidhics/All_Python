from sys import flags
import cv2
from cv2 import imread
import numpy as np
img1=imread("ImageQuery/box.jpg",0)#0---> use for gray scale
img2=imread("ImageTrain/box.jpg",0)

# orb = cv2.ORB_create(nfeatures=1000)#---> by default there is 500 matches you are increasing the matches
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# print(des1)
# print(des1[0])
print(len(des1[0]))
print(des1.shape) #(200,32) --> means finding 200 features in image, and describe it in 32 values

img1Kp1 = cv2.drawKeypoints(img1, kp1, None)
img2Kp2 = cv2.drawKeypoints(img2, kp2, None)

bf = cv2.BFMatcher()
matches=bf.knnMatch(des1,des2,k=2)
good=[]
for m,n in matches:
    if m.distance<0.75*n.distance:
        good.append([m])
    
print(len(good))

img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)


# cv2.imshow('img1 kp1',img1Kp1)
# cv2.imshow('img2 kp2',img2Kp2)
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
cv2.imshow("img3",img3)
cv2.waitKey(0)