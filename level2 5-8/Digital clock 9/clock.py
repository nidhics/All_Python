# from tkinter import *

# from time import strftime

# root = Tk()

# root.title('Digital clock')

# def clock():
# 	tick = strftime('%H:%M:%S %p')

# 	label.config(text =tick)

# 	label.after(1000, clock)

# label = Label(root, font =('sans', 80), background = 'black', foreground = 'red')

# label.pack(anchor= 'center')

# clock()
# mainloop()


from tkinter import *
import time
root = Tk()
root.title("Digital Clock")
def clock() : 
    tick = time.strftime("%H : %M : %S %p")
    # tick = time.strftime("%X")
    label.config(text = tick) 
    label.after(1000,clock)


label1 = Label(root,text = "Digital Clock",font = ("arial",20),bg = "yellow",fg = "blue")
label = Label(root,font = ("arial",20),background = "black",foreground = "red")
btn=Button(root, text="This is Button widget", fg='blue')

txtfld=Entry(root, text="This is Entry Widget", bd=5)

# label1.place(x=50,y=40)
label.place(x=45,y=100)
btn.place(x=80, y=200)
txtfld.place(x=80, y=150)
label1.pack()
# label.pack()
# btn.pack()
clock()
root.configure(background="#00ffff")#hexa decimal gb color values
root.geometry("400x250+300+400")
root.mainloop()

