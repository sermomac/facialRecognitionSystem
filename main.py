import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os, sys, subprocess
from student import Student
from help import Help
from developer import Developer
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # Header images
        # First image
        img = Image.open(r"images/facial.jpeg")
        img = img.resize((560, 130), Image.ANTIALIAS)
        self.ph = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.ph)
        f_lbl.place(x=0, y=0, width=560, height=130)

        # Second image
        img1 = Image.open(r"images/1.jpeg")
        img1 = img1.resize((560, 130), Image.ANTIALIAS)
        self.ph1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.ph1)
        f_lbl1.place(x=560, y=0, width=560, height=130)

        # Third image
        img2 = Image.open(r"images/4.png")
        img2 = img2.resize((560, 130), Image.ANTIALIAS)
        self.ph2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.ph2)
        f_lbl2.place(x=1120, y=0, width=560, height=130)

        # Background image
        img3 = Image.open(r"images/2.jpeg")
        img3 = img3.resize((1700, 800), Image.ANTIALIAS)
        self.ph3 = ImageTk.PhotoImage(img3)

        b_img = Label(self.root, image=self.ph3)
        b_img.place(x=0, y=130, width=1700, height=800)


        # Title
        title = Label(b_img, text='FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title, font=('Lucida Calligraphy', 20, 'bold'), bg='white', fg='red')
        lbl.place(x=0, y=0, width=150, height=45)
        time()

        # Footer
        title = Label(b_img, text='MINI PROJECT 2021', font=('Lucida Calligraphy', 18, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=750, width=1700, height=20)

        # ================================= Function Buttons =============================
        def student_details():
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)

        def train_data():
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)

        def open_img():
            self.root.filename = filedialog.askopenfilename(initialdir='data/')
            # os.popen('data')
            # os.startfile('data')

        def face_data():
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition(self.new_window)

        def attendance_data():
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)

        def developer():
            self.new_window = Toplevel(self.root)
            self.app = Developer(self.new_window)

        def help():
            self.new_window = Toplevel(self.root)
            self.app = Help(self.new_window)

        def exit():
            self.exit = tkinter.messagebox.askyesno('Face Recognition','Are you sure you want to exit!?')
            if self.exit >0:
                self.root.destroy()
            else:
                return
        # ================================================================================

        # Student link----->
        img4 = Image.open(r"images/students.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.ph4 = ImageTk.PhotoImage(img4)
        # Text
        b1 = Button(b_img, image=self.ph4, command=student_details, cursor='hand2')
        b1.place(x=150, y=100, width=220, height=220)

        b1_1 = Button(b_img, text='Student details', command=student_details, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b1_1.place(x=150, y=300, width=220, height=40)

        # Detect Face link----->
        img5 = Image.open(r"images/face.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.ph5 = ImageTk.PhotoImage(img5)
        # Text
        b2 = Button(b_img, image=self.ph5, command=face_data, cursor='hand2')
        b2.place(x=525, y=100, width=220, height=220)

        b2_1 = Button(b_img, text='Face Detector', command=face_data, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=525, y=300, width=220, height=40)

        # Attendance link----->
        img6 = Image.open(r"images/attendace.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.ph6 = ImageTk.PhotoImage(img6)
        # Text
        b2 = Button(b_img, image=self.ph6, command=attendance_data,cursor='hand2')
        b2.place(x=925, y=100, width=220, height=220)

        b2_1 = Button(b_img, text='Attendance', command=attendance_data, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=925, y=300, width=220, height=40)

        # Help Desk link----->
        img7 = Image.open(r"images/help.jpeg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.ph7 = ImageTk.PhotoImage(img7)
        # Text
        b2 = Button(b_img, image=self.ph7, command=help, cursor='hand2')
        b2.place(x=1300, y=100, width=220, height=220)

        b2_1 = Button(b_img, text='Help Desk', command=help, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=1300, y=300, width=220, height=40)

        # Train data link----->
        img8 = Image.open(r"images/data.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.ph8 = ImageTk.PhotoImage(img8)
        # Text
        b2 = Button(b_img, image=self.ph8, command=train_data, cursor='hand2')
        b2.place(x=150, y=440, width=220, height=220)

        b2_1 = Button(b_img, text='Train Data', command=train_data, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=150, y=650, width=220, height=40)

        # Photos link----->
        img9 = Image.open(r"images/photos.jpeg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.ph9 = ImageTk.PhotoImage(img9)
        # Text
        b2 = Button(b_img, image=self.ph9, command=open_img, cursor='hand2')
        b2.place(x=525, y=450, width=220, height=220)

        b2_1 = Button(b_img, text='Photos', command=open_img, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=525, y=650, width=220, height=40)

        # Developer link----->
        img10 = Image.open(r"images/dev.jpeg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.ph10 = ImageTk.PhotoImage(img10)
        # Text
        b2 = Button(b_img, image=self.ph10, command=developer, cursor='hand2')
        b2.place(x=925, y=450, width=220, height=220)

        b2_1 = Button(b_img, text='Developer', command=developer, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=925, y=650, width=220, height=40)

        # Exit link----->
        img11 = Image.open(r"images/exit.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.ph11 = ImageTk.PhotoImage(img11)
        # Text
        b2 = Button(b_img, image=self.ph11, command=exit, cursor='hand2')
        b2.place(x=1300, y=450, width=220, height=220)

        b2_1 = Button(b_img, text='Exit', command=exit, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=1300, y=650, width=220, height=40)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
