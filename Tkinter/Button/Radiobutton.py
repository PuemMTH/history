from tkinter import *
from tkinter import messagebox 
mw = Tk()
mw.title("Simple GUI")
mw.geometry('300x300')
lb = Label(mw,text="==================================").pack()
lb = Label(mw,text="Radio button").pack()
def sex():
    if r1.var.get() == 1:
        sex_get = "male"
    else:
        sex_get = "female"
    messagebox.showinfo("Show Sex","you is sex %s"%(sex_get))
c1 = c2 = IntVar()
r1 = Radiobutton(mw,text='male',variable=c1,value=1)
r1.var = c1
r1.pack()
r2 = Radiobutton(mw,text='female',variable=c2,value=2)
r2.var = c2
r2.pack()
bt = Button(mw,text='Save $',bg='blue',fg='white',activebackground='green',command=sex).pack()
lb = Label(mw,text="==================================").pack()

mw.mainloop()