
'''
Team name   : Glacius
Project Name: Phonebook Management System
Description : A login page with username and password: SunnyReddy / password
'''

from tkinter import *
from tkinter import messagebox

def login():
    userid=entry1.get()
    password=entry2.get()

    if (userid=="" and password==""):
        messagebox.showinfo("","please provide your credentials")

    elif (userid=="SunnyReddy" and password=="password"):
        messagebox.showinfo("","You Have Logged In Successfully")

    else:
        messagebox.showinfo("","you have entered incorrect credentials")

root=Tk()
root.title("Welcome to Login Page")
root.geometry("300x200")

global Entry1
global Entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=5)
entry2.place(x=140,y=70)

Button(root,text="login",command=login,height=3,width=13,bd=6,bg = "black", fg = "white").place(x=100,y=120)

root.mainloop()
        
