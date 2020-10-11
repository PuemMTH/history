from tkinter import *
from tkinter import messagebox 
import os

mw = Tk()
mw.title("Simple GUI")
mw.geometry('300x130')


labelframe = LabelFrame(mw, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
lable_1 = Label(labelframe, text="Form keep data").pack()

name = StringVar()
lable_1 = Label(labelframe, text="Username").pack()
input_name = Entry(labelframe,textvariable=name).pack()

def prints():
    names = name.get()
    print(names)
    file = open(names, "w")
    file.write(names)
    file.close()
def shows():
    list_of_files = os.listdir()
    print(list_of_files)
bt = Button(labelframe,text="Saves",command=prints).pack(side = LEFT)
bts = Button(labelframe,text="Shows",command=shows).pack(side = RIGHT)

# redbutton = Button(labelframe, text="Red", fg="red").pack(side = LEFT)
# greenbutton = Button(labelframe, text="Brown", fg="brown").pack(side = RIGHT)
# bluebutton = Button(labelframe, text="Blue", fg="blue").pack(side = BOTTOM)
mw.mainloop()




 
