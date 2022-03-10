#send our new image to our model
import numpy as np
import cv2
import pickle

#######################################

width =640
height=480
threshold=0.50
#######################################

cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)


pickle_in=open("model_trained.p","rb")
model=pickle.load(pickle_in)



def preProcessing(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)#it equalize the light evenly
    img=img/255 # normalize the value ---> in gray scale vlaue is in between 0-255, instead it should be 0-1, better for training pocess
    return img


while True:
    success, imgOriginal= cap.read()
    img=np.asarray(imgOriginal)
    img=cv2.resize(img,(32,32))
    img=preProcessing(img)
    # cv2.imshow("Pocessed Image", img)
    img=img.reshape(1,32,32,1)
    #predict
    classIndex=int(model.predict_classes(img))
    # print(classIndex)

    predictions= model.predict(img) #to get the probability of prediction
    # print(predictions)
    probVal=np.amax(predictions)
    print(classIndex,"------------>",probVal)
    
    if probVal>threshold:

        cv2.putText(imgOriginal,str(classIndex)+" ---> " +str(probVal),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),4)
    cv2.imshow("original image",imgOriginal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
