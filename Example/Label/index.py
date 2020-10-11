from tkinter import *
from tkinter import messagebox 

mw = Tk()
mw.title("Simple From GUI")
mw.geometry('350x300+500+100')
mw.configure(background='wheat1')
mw.iconbitmap('puemmth.ico')
la = Label(mw, text="Form Register" ,bg="gold", width=30)
la.grid(row=0, 
        columnspan=2, 
        sticky="news",
        ipady=20)

frame = Frame(mw)
frame.grid(columnspan=2,column=0)

email = StringVar()
password = StringVar()
phone = StringVar()
sex = StringVar()
Label(frame, text="Email:").grid(row=2,column=0)
input_email= Entry(frame,textvariable=email).grid(row=2,column=1)
Label(frame, text="Password:").grid(row=2,column=2)
input_password = Entry(frame,textvariable=password).grid(row=2,column=3)
Label(frame, text="Phone:").grid(row=3,column=0)
input_phone = Entry(frame,textvariable=phone).grid(row=3,column=1)
Label(frame, text="Sex:").grid(row=3,column=2)
input_sex= Entry(frame,textvariable=sex).grid(row=3,column=3)

input_sex= Entry(frame,textvariable=None).grid(row=3,column=3)
Label(frame, text="None:").grid(row=4,column=0)
input_phone = Entry(frame,textvariable=None).grid(row=4,column=1)
Label(frame, text="None:").grid(row=4,column=2)
input_None= Entry(frame,textvariable=None).grid(row=4,column=3)
# grid(row=3,column=3)
def save():
    email_get = email.get()
    password_get = password.get()
    phone_get = phone.get()
    sex_get = sex.get()
    messagebox.showinfo("Answer","Email: %s\nPassword: %s\nPhone: %s\nSex: %s"%(email_get,password_get,phone_get,sex_get))
def lists():
    pass
btn_male = Button(mw, text="Save", bg="deep sky blue", width=20, command=save)
btn_male.grid(row=100,
              column=0,
              ipady=20)
btn_female = Button(mw, text="List", bg="hot pink", width=20, command=lists)
btn_female.grid(row=100,
                column=1,
                ipady=20)
mw.mainloop()