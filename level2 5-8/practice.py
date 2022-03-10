# word="nidhi"
# for char in word:
#     print(char)

# dict={"name":"nidhi"}
# # print(dict)

# dict.update({"name":"sagar"})
# print(dict)


# string="is a good girl, and  become a great coder one day. nidhi"
# sub_string="ni"
# print(string.find(sub_string))
# if string.find(sub_string)==-1:
#     print("not found")
# else:
#     print("find")



# for i in range(1000,0,-1):
#     print(i)



# a=2
# b=3
# a,b=b,a
# print(a,b)
#------------------------------------------exception handling-------------------------
# num1=input("enter num1: ")
# num2=input("enter num2: ")
# # try:
# #     print("sum",int(num1)+int(num2))
# # except Exception as e:
# #      print(e)
# # print("hi")

# try:
#     print("sum",int(num1)+int(num2))
# finally:
#     print("lo")
# except:
#      print("hi")


# str="hi"
# print(str.upper())

#-------------------------covid data handling-------------------------


# a=["i am a good girl","i love coding","please let me study","i donot like house chores"]
# b="i am a good girl"
# if(b in a):
#     print("present")

# d2={"apple mango":"burger","b":"pizza","c":"indian"}
# if "apple mango" in d2:
#     print("present hai")
# # print(d2.keys())
# print(d2.values())
# print(d2.items())

# list1=[["a",1],["b",3],["c",4]]
# for i in list1:
#     print(i)

# for name,book in list1:
#     print(name," reads ",book)


# dict1=dict(list1)
# print(dict1)
# print(dict1.items())
# for name,book in dict1.items():
#     print(name,"reads",book,"book in a day")



# from turtle import *
# # t=Turtle()
# # s=Screen()
# # s.title("Fidget Spinner")
# # s.bgcolor("gold")
# # t.shape("turtle")
# # t.color("silver")
# # done()
# turn=0
# def spinner():
#     # clear()
#     angle=turn/10
#     right(angle)
#     forward(100)
#     dot(120, "blue")
#     back(100)
#     right(120)
#     forward(100)
#     dot(120, "magenta")
#     back(100)
#     right(120)
#     forward(100)
#     dot(120, "yellow")
#     back(100)
#     # right(120)
#     update()
# def animate():
#     global turn
#     spinner()
#     ontimer(animate, 10)
# def flick():
#     global turn
#     turn+=10
#     pass
# setup(420, 420)
# tracer(False)
# width(20)
# onkey(flick, "space")
# listen()
# animate()
# done()

# try :
#     print(x)
# except NameError:
#     print("var is not defined")
# except:
#     print("somthing went wrong")

def crossProduct(seq1, seq2):
    if not seq1 or not seq2:
        raise ValueError("Sequence arguments must be non-empty")
    return [ (x1, x2) for x1 in seq1 for x2 in seq2 ]


crossProduct([678,687])