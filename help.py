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


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # ===========================================================
        # Title
        title = Label(self.root, text='HELP DESK',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Images
        top_img = Image.open(r"images/helpDesk.jpeg")
        top_img = top_img.resize((1700, 860), Image.ANTIALIAS)
        self.ph_top = ImageTk.PhotoImage(top_img)

        img1 = Label(self.root, image=self.ph_top)
        img1.place(x=0, y=45, width=1700, height=860)

        # Email info
        Name = Label(self.root, text='sermomac@gmail.com', font=('Lucida Calligraphy', 20, 'bold'))
        Name.place(x=720, y=850)


if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()
