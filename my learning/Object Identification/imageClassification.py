from sys import flags
import cv2
import numpy as np
import os

orb = cv2.ORB_create()

# importing images from folder
path="ImageQuery"
images=[]
classNames=[]
myList=os.listdir(path)#put the images in list form on particular path

# print(myList)

for cl in myList:
    imgCur=cv2.imread(f"{path}/{cl}",0)
    images.append(imgCur)
    # print(os.path.splitext(cl))#in tuple saprate the file name and extention
    classNames.append(os.path.splitext(cl)[0])#spliting extention

print(classNames)

# creating descriptor for each images




def findDescriptor(images):
    desList=[]
    for img in images:

        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList    




def findID(img,desList,thresh=8):#thresh is parameter bydefault it is 15 if user define it will change
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList=[]
    finalVal=-1#cause 0 is the index in match list array

    try:
        for des in desList:
            matches=bf.knnMatch(des,des2,k=2)
            good=[]
            for m,n in matches:
                if m.distance<0.75*n.distance:
                    good.append([m])
                
            # print(len(good))
            matchList.append(len(good))
    except:
        print("error")
    print(matchList)  #going to print how many matches find from each image in ImageQuery folder

    if len(matchList) != 0:
        if max(matchList)>thresh:
            finalVal=matchList.index(max(matchList))

    return finalVal



desLis=findDescriptor(images)

# print(len(desLis))
# print(desLis[0])


# access the web cam to show the objects

cap= cv2.VideoCapture(0)
while True:
    success, img2=cap.read()
    imgOriginal=img2.copy()
    img2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id= findID(img2,desLis)
    if id != -1:
        cv2.putText(imgOriginal,classNames[id],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    cv2.imshow("img2", imgOriginal)
    cv2.waitKey(1)



# img1=cv2.imread("ImageQuery/box.jpg",0)#0---> use for gray scale
# img2=cv2.imread("ImageTrain/box.jpg",0)

# # orb = cv2.ORB_create(nfeatures=1000)#---> by default there is 500 matches you are increasing the matches
# orb = cv2.ORB_create()

# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)
# print(des1.shape) #(200,32) --> means finding 200 features in image, and describe it in 32 values

# img1Kp1 = cv2.drawKeypoints(img1, kp1, None)
# img2Kp2 = cv2.drawKeypoints(img2, kp2, None)

# bf = cv2.BFMatcher()
# matches=bf.knnMatch(des1,des2,k=2)
# good=[]
# for m,n in matches:
#     if m.distance<0.75*n.distance:
#         good.append([m])
    
# print(len(good))

# img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)


# cv2.imshow('img1 kp1',img1Kp1)
# cv2.imshow('img2 kp2',img2Kp2)
# cv2.imshow('img1',img1)
# cv2.imshow('img2',img2)
# cv2.imshow("img3",img3)
# cv2.waitKey(0)