from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

myData = []

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # ===========================================================
        # Title
        title = Label(self.root, text='DEVELOPER',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Images
        top_img = Image.open(r"images/dataset.jpeg")
        top_img = top_img.resize((1700, 860), Image.ANTIALIAS)
        self.ph_top = ImageTk.PhotoImage(top_img)

        img1 = Label(self.root, image=self.ph_top)
        img1.place(x=0, y=45, width=1700, height=860)

        # Main Frame
        main_frame = Frame(img1, bd=2, bg='white')
        main_frame.place(x=1150, y=20, width=500, height=800)

        # Logo
        top_img1 = Image.open(r"images/BU.png")
        top_img1 = top_img1.resize((200, 200), Image.ANTIALIAS)
        self.ph_top1 = ImageTk.PhotoImage(top_img1)

        img2 = Label(main_frame, image=self.ph_top1)
        img2.place(x=150, y=20, width=200, height=200)

        # BU
        BU = Label(main_frame, text='Bangalore University', font=('Lucida Calligraphy', 20, 'bold'))
        BU1 = Label(main_frame, text='Jnana Bharathi Campus', font=('Lucida Calligraphy', 20, 'bold'))
        BU.place(x=150, y=250)
        BU1.place(x=130, y=280)

        # Images frame
        top_img2 = Image.open(r"images/Mac.JPG")
        top_img2 = top_img2.resize((200, 200), Image.ANTIALIAS)
        self.ph_top2 = ImageTk.PhotoImage(top_img2)

        img3 = Label(main_frame, image=self.ph_top2)
        img3.place(x=150, y=350, width=200, height=200)

        # Developer info
        Name = Label(main_frame, text='Sergio Moises Macarringue', font=('Lucida Calligraphy', 20, 'bold'))
        Name.place(x=110, y=560)
        Profession= Label(main_frame, text='Masters of Computer Application', font=('Lucida Calligraphy', 20, 'bold'))
        Profession.place(x=80, y=590)
        Project = Label(main_frame, text='Mini Project 2022 - V MCA', font=('Lucida Calligraphy', 20, 'bold'))
        Project.place(x=112, y=620)





if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()
