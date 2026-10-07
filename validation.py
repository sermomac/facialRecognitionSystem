import tkinter
from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.title("Python Validation")


heading = Label(text=  'Python Form validation', fg='black', bg='grey', width='500', height='3').pack()


def error():
    screen1 = Toplevel(screen)
    screen1.geometry('150x50')
    screen1.title('Warning')
    Label(screen1, text='All fields are required', fg='red').pack()

def register():
    username_text = username.get()
    password_text = password.get()

    if username_text == "" and password_text == "":
        error()
    else:
        Label(text='User registered successfully').place(x=150, y=250)


def reset():
    pass

Label(text='Username * ').place(x=15, y=70)
Label(text='Password * ').place(x=15, y=140)

username = StringVar()
password = StringVar()

Entry(screen, textvariable='username'). place(x=15, y=100)
Entry(screen, textvariable='password'). place(x=15, y=170)

Button(screen,  text='Register', width='7', bg='grey', command=register).place(x=20, y=210)
Button(screen,  text='Reset', width='7', bg='grey', command='').place(x=120, y=210)

screen.mainloop()

