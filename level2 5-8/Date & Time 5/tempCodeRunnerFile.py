import datetime

def getDate():
    return datetime.datetime.now()

t=getDate()

# print(t)
print(t.strftime("%X"), t.strftime("%p")) # 11:19:49 AM
