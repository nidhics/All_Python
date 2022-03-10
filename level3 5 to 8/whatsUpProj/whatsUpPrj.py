import datetime
import pywhatkit
import pyautogui as pg
import schedule
import time

def job():
    try:
        now =datetime.datetime.now()
        print(now.hour,now.minute+2 )
        pywhatkit.sendwhatmsg("+919711926888","hi I am nidhi",now.hour,now.minute+2,32)
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("tab")
        pg.press("enter")
        print("Successfully Sent!")
 
    except:
   
        print("An Unexpected Error!")


# job()
# schedule.every(10).seconds.do(job)
schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)