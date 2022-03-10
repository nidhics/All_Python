from turtle import *
state = {'turn': 0}
turn=0

def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)

    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    # if state['turn']>0:
    #     state['turn']-=1
    spinner()
    ontimer(animate, 20)

def flick():
    state['turn']+=10

setup(620, 620,None,None)
# 620*620 is size of window, None, none window will appear in center of desktop.
tracer(False)#going to visible how it's drawing
width(20)
speed(1)
onkey(flick, 'space')
listen()
# spinner()
animate()
done()

# ------------------------------------------------my code
# from turtle import *

# turn=0

# def spinner():
#     clear()
#     angle = turn/10
#     right(angle)
#     forward(100)
    
#     dot(120, 'red')
#     back(100)
#     right(120)
#     forward(100)

#     dot(120, 'green')
#     back(100)
#     right(120)
#     forward(100)
    
#     dot(120, 'blue')
#     back(100)
#     right(120)
#     update()

# def animate():
#     global turn #now, this animate function have a permission to change global variable 'turn'
#     # if we donot write this line animate function don't have permission to change global variable
#     if turn>0:
#         turn-=1   
#     spinner()
#     ontimer(animate, 20)

# def flick():
#     global turn
#     turn+=10

# setup(620, 620,None,None)
# # 620*620 is size of window, None, none window will appear in center of desktop.
# tracer(False)#going to visible how it's drawing
# width(20)
# speed(1)
# onkey(flick, 'space')
# listen()
# # spinner()
# animate()
# done()

# ------------------------------------------------------design
# from turtle import *

# def spinner():

#     forward(100)

#     dot(120,"red")
#     back(100)
#     right(120)
#     forward(100)

#     dot(120,"blue")
#     back(100)
#     right(120)
#     forward(100)

#     dot(120,"green")
#     back(100)
#     right(120)
#     # forward(100)
#     update()
# setup(500,500,None,None)
# # tracer(False)
# width(20)
# speed(1)
# spinner()
# done()