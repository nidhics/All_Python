from tkinter import *

# root=Tk()
# button1 = Button(root,text="Hi",width=17,height=7,font=('Helvetica  10'))
# button1.grid(column=1,row=0)
# root.mainloop()


class Warspyking(Frame):
    '''A button that has it's width and height set in pixels'''
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

#example usage:
MyWindow = Tk()
MyWindow.geometry("500x550")

from itertools import cycle
fonts = cycle((('Helvetica', '11'),('Helvetica', '15'),('Helvetica', '20')))
def chg():
    button.config(font=next(fonts))

button = Warspyking(MyWindow,text="Click me!",width=200,height=100 ,font=next(fonts), command=chg)
button.grid(row=1, column=1)

MyWindow.mainloop()