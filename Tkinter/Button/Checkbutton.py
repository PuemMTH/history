from tkinter import *
from tkinter import messagebox 
mw = Tk()
mw.title("Simple GUI")
mw.geometry('300x300')
# mw.configure(background='red')
def confirm():
    # messagebox.showwarning('Inserth','มองหาพ่องเหรอ')
    messagebox.showerror('Error','it error infomation')
# bt = Button(mw, text='Simple', bg='green', fg='white', command=confirm)
# bt.place(x=16,y=16)
lb = Label(mw,text="==================================").pack()
lb = Label(mw,text="Order button").pack()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
cb1 = Checkbutton(mw,text='Noddle : 10$',variable=v1,onvalue=1,offvalue=0)
cb1.var = v1
cb1.pack()
cb2 = Checkbutton(mw,text='Noddle : 20$',variable=v2,onvalue=1,offvalue=0)
cb2.var = v2
cb2.pack()
cb3 = Checkbutton(mw,text='Noddle : 30$',variable=v3,onvalue=1,offvalue=0)
cb3.var = v3
cb3.pack()
def deal():
    if cb1.var.get() == 1:
        cb1_get = 10
    else:
        cb1_get = 0
    if cb2.var.get() == 1:
        cb2_get = 20
    else:
        cb2_get = 0
    if cb3.var.get() == 1:
        cb3_get = 30
    else:
        cb3_get = 0
    sum = cb1_get + cb2_get + cb3_get
    messagebox.showinfo('Order bye','Total : %s'%(str(sum)))
bt = Button(mw,text='Order $',bg='blue',fg='white',activebackground='green',command=deal).pack()
lb = Label(mw,text="==================================").pack()

mw.mainloop()