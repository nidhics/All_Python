import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense
import tensorflow as tf
# from tensorflow import keras
# from keras.optimizers import Adam
# from tensorflow.keras.optimizers import Adam

import pickle

path ="../TextIdentification/my_num_dataset"

myList=os.listdir(path)
# print(myList)

images=[]
classNo=[]

test_ratio=0.2
validation_ratio=0.2
imageDimention=(32,32,3)


noOfClasses=len(myList)

batchSizeVal=50
epochsVal=10
stepsPerEpochsVal=2000 # change it to 2000 later




print("Total Num of classes : ",noOfClasses )

print("importing classes.......")
for x in range(0,noOfClasses):
    myPicList=os.listdir(path+"/"+str(x))
    # print(x,"\n",myPicList)
    for y in myPicList:
        curImg=cv2.imread(path+"/"+str(x)+"/"+y)
        curImg=cv2.resize(curImg,(imageDimention[0],imageDimention[1]))
        images.append(curImg)
        classNo.append(x)#contains class id each of this images
    print(x,end=" ")
print("\r")
print("num of images imported :",len(images))
# print(len(classNo))

# converted the images in array

images=np.array(images)
print (images.shape)
classNo=np.array(classNo)
print(classNo) #contains id 0 to 9


# ############################# spiliting DATA ###################################
# first whole data divide in 80% (train)to 20% (test)
#then whole 80% of train data further divide into 80% train and 20% for validation
x_train,x_test,y_train,y_test=train_test_split(images,classNo,test_size=test_ratio)#shuffle whole images first, and then spilit in training and testing
print(x_train.shape)
print(x_test.shape)
# print(y_train.shape)#contain id
# print(y_test.shape)#contain id
x_train,x_validation,y_train,y_validation=train_test_split(x_train,y_train,test_size=test_ratio)#further spilit for validation
print(x_train.shape)
print(x_validation.shape)


########################## How many images for each class #######################
# print(np.where(y_train==0))#give all the index where class is 0
# print(np.where(y_train==1))#give all the index where class is 1

# print(np.where(y_train==0)[0])#give all the value is in array

# print(len(np.where(y_train==0)[0]))#telling how many samples for class 0


numOfSamples=[]
for x in range(noOfClasses):
    # print(len(np.where(y_train==x)[0]))
    numOfSamples.append(len(np.where(y_train==x)[0]))

print(numOfSamples)


####################### show it in a bar chart to see weather the number of images of each classes is even or not############################

plt.figure(figsize=(10,5))# size of the window of matplotlib
plt.bar(range(noOfClasses),numOfSamples)
plt.title("Num of images for each class")
plt.xlabel("classes")
plt.ylabel("num of images")
plt.show()


###########################preprocessing the image ###########################################

def preProcessing(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.equalizeHist(img)#it equalize the light evenly
    img=img/255 # normalize the value ---> in gray scale vlaue is in between 0-255, instead it should be 0-1, better for training pocess
    return img

# print(x_train.shape)#before preprocessing it have 3 channels

########### preprocessed single image

# img=preProcessing(x_train[0])
# img=cv2.resize(img,(300,300))
# cv2.imshow("preprocessed image", img )
# cv2.waitKey(0)

################ preprocessing all the images, take each image from x_train and send it to preprocessing function one by one
# map(preProcessing,x_train)

x_train=np.array(list(map(preProcessing,x_train)))

# print(x_train.shape)#after preprocessing it have 1 channels

# img=x_train[0]
# img=cv2.resize(img,(300,300))
# cv2.imshow("preprocessed image", img )
# cv2.waitKey(0)

x_test=np.array(list(map(preProcessing,x_test)))
x_validation=np.array(list(map(preProcessing,x_validation)))


#################################### depth of one in our images for CNN ##############################
# print(x_train.shape)#before reshape
x_train=x_train.reshape(x_train.shape[0],x_train.shape[1],x_train.shape[2],1)
# print(x_train.shape)#after reshape
x_test=x_test.reshape(x_test.shape[0],x_test.shape[1],x_test.shape[2],1)
x_validation=x_validation.reshape(x_validation.shape[0],x_validation.shape[1],x_validation.shape[2],1)


#################################### Augmentation of image using keras ##############################
dataGen=ImageDataGenerator(width_shift_range=0-1,height_shift_range=0.1,zoom_range=0.2,shear_range=0.1,rotation_range=10)

dataGen.fit(x_train)#an iterator, returning batches of image samples when requested.

y_train=to_categorical(y_train,noOfClasses)
y_test=to_categorical(y_test,noOfClasses)
y_validation=to_categorical(y_validation,noOfClasses) # convert integers to binary

def myModel():#CNN 
    noOfFilters=60
    sizeOfFilter1=(5,5)
    sizeOfFilter2=(3,3)
    sizeOfPool=(2,2)
    noOfNode=500

    model=Sequential()
    model.add((Conv2D(noOfFilters,sizeOfFilter1,input_shape=(imageDimention[0],imageDimention[1],1),activation="relu")))
    model.add((Conv2D(noOfFilters,sizeOfFilter1,activation="relu")))

    model.add(MaxPooling2D(pool_size=sizeOfPool))
    
    model.add((Conv2D(noOfFilters//2,sizeOfFilter2,activation="relu")))
    model.add((Conv2D(noOfFilters//2,sizeOfFilter2,activation="relu")))
    
    model.add(MaxPooling2D(pool_size=sizeOfPool))

    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(noOfNode,activation="relu"))
    model.add(Dense(noOfClasses,activation="softmax"))#final layer

    # model.compile(Adam(lr=0.001),loss="categorical_crossentropy",metrics=['accuracy'])#adam is optimizer,learning rate=0.0001
    # model.compile(loss='categorical_crossentropy', optimizer='adam')
    model.compile(tf.keras.optimizers.Adam(lr=0.001),loss="categorical_crossentropy",metrics=['accuracy'])#adam is optimizer,learning rate=0.0001
    
    return model


model=myModel()

print(model.summary())



#-------------------------------run the training and request the augmented images in batches

history=model.fit_generator(dataGen.flow(x_train,y_train,batch_size=batchSizeVal),
                    steps_per_epoch=stepsPerEpochsVal, 
                    epochs=epochsVal,
                    validation_data=(x_validation,y_validation),
                    shuffle=1)

plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training','validation'])#lines showing in graph
plt.title("loss")
plt.xlabel('no of epochs')

plt.figure(2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.legend(['training','validation'])#lines showing in graph
plt.title("loss")
plt.xlabel('no of epochs')

plt.show()
score=model.evaluate(x_test,y_test,verbose=0)
print("Test Score = ",score[0])
print("Test Accuracy = ",score[1])


# -------------saving the model which we have trained, so that we can use it ------------------------------


pickle_out=open("model_trained.p","wb")
pickle.dump(model,pickle_out)
pickle_out.close()