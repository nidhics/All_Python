import time as t
from pygame import mixer


file_full_path= r"D:\\programming with python\\my learning\\Healthy Programmer\\all.txt"
# extra fwd slash used for removing the escape character effect


def log_entry(msg):
     with open(file_full_path,"a") as f:
        f.write(f"\n {msg} : {t.asctime()}")


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    a=input()
    if(a==stopper):
        mixer.music.stop()
            
if __name__=="__main__":
    watertime=10
    eyeEx=20
    phyEx=30

    initWater=t.time()
    initEye=t.time()
    initPhy=t.time()

    while True:

        calTimeWater=t.time()-initWater 
        if(calTimeWater>10):

            print("water drinking time, write 'drank' to stop alarm")
            musiconloop(r"D:\\programming with python\\my learning\\Healthy Programmer\\mp3 files\\waterfall.mp3","drank")
            log_entry("water")
            initWater=t.time()
            # print(initPhy)

        calTimeEye=t.time()-initEye 
        if(calTimeEye>20):
            print("Eye exercise time, write 'done' to stop alarm")
            musiconloop("my learning\Healthy Programmer\mp3 files\waterfall.mp3","done")
            log_entry("Eye Exercise")
            initEye=t.time()
            # print(initEye)

        calTimePhy=t.time()-initPhy 
        if(calTimePhy>30):
            print("physical exercise time.write 'did' to stop alarm")
            musiconloop("my learning\Healthy Programmer\mp3 files\waterfall.mp3","did")
            
            log_entry("Physical Exercise")
            initPhy=t.time()
            # print(initPhy)


        
