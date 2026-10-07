from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
import sys
import subprocess
from tkmacosx import Button
from student import Student
from help import Help
from developer import Developer
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    win = Tk()
    obj = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Login')

        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_new_pass = StringVar()

        # ================================ Functions ====================================================

        def callback():
            if name.isalnum():
                return True
            if name == "":
                return True
            else:
                messagebox.showerror('Error', 'Invalid '+name[-1])

        def login():
            if usertext.get() == '' or pwtext.get() == '':
                messagebox.showerror('Error', 'All fields required')
            elif usertext.get() == 'mac' and pwtext.get() == '123':
                messagebox.showinfo('Success', 'Welcome to the Admin module!')
                new_window = Toplevel(root)
                app = Face_Recognition_System(new_window)
            else:
                conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    passwd=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME"))
                my_cursor = conn.cursor()
                my_cursor.execute('SELECT * FROM register WHERE email=%s AND password=%s', (
                    self.var_email.get(),
                    self.var_pass.get()
                ))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror(
                        'Error', 'Invalid Username and Password')
                else:
                    open_main = messagebox.askyesno(
                        'YesNo', 'Access Student module?')
                    if open_main > 0:
                        new_window = Toplevel(root)
                        app = Face_Recognition_System1(new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()

        def register_window():
            new_windpw = Toplevel(root)
            app = Register(new_windpw)

        def reset_password():
            if self.var_securityQ == 'Select':
                messagebox.showerror(
                    "Error", 'Please select security question!', parent=self.root2)
            elif self.var_securityA.get() == '':
                messagebox.showerror(
                    "Error", 'Please enter the security answer!', parent=self.root2)
            elif self.var_new_pass.get() == '':
                messagebox.showerror(
                    "Error", 'Please enter the new password!', parent=self.root2)
            else:
                conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    passwd=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME")
                )
                my_cursor = conn.cursor()
                query = 'SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s'
                value = (usertext.get(), self.var_securityQ.get(),
                         self.var_securityA.get(), )
                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror(
                        "Error", 'Please enter the correct answer!', parent=self.root2)
                else:
                    queryy = 'UPDATE register SET password=%s WHERE email=%s'
                    values = (self.var_new_pass.get(), usertext.get())
                    my_cursor.execute(queryy, values)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        'Info', 'Password has been reset, please login with the new password', parent=self.root2)
                    self.root2.destroy()

        def forgot_password():
            if usertext.get() == '':
                messagebox.showerror(
                    'Error', 'Enter your E-mail address to reset the password')
            else:
                conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    passwd=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME")
                )
                my_cursor = conn.cursor()
                query = 'SELECT * FROM register WHERE email=%s'
                value = (usertext.get(), )
                my_cursor.execute(query, value)

                row = my_cursor.fetchone()
                # print(row)
                if row is None:
                    messagebox.showerror(
                        "Error", 'Please enter the correct E-mail address!')
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title('Forgot Password')
                    self.root2.geometry('400x500')

                    l = Label(self.root2, text='FORGOT PASSWORD', font=(
                        'Lucida Calligraphy', 22, 'bold'), fg='red', bg='white')
                    l.place(x=0, y=10, relwidth=1)

                    question = Label(self.root2, text='Select Security Question', font=(
                        'Lucida Calligraphy', 22, 'bold'), bg='white')
                    question.place(x=60, y=80)

                    combo = ttk.Combobox(self.root2, textvariable=self.var_securityQ, font=(
                        'Lucida Calligraphy', 22), state='readonly')
                    combo['values'] = ('Select', 'Your birth place', 'Your favourite city',
                                       'Your favourite car', 'Your bestfriend name')
                    combo.place(x=60, y=120, width=300)
                    combo.current(0)

                    answer = Label(self.root2, text='Security Answer', font=(
                        'Lucida Calligraphy', 22, 'bold'), bg='white')
                    answer.place(x=60, y=190)
                    atext = ttk.Entry(self.root2, textvariable=self.var_securityA, font=(
                        'Lucida Calligraphy', 22))
                    atext.place(x=60, y=220, width=300)

                    pw = Label(self.root2, text='New Password', font=(
                        'Lucida Calligraphy', 22, 'bold'), bg='white')
                    pw.place(x=60, y=280)
                    self.nptext = ttk.Entry(
                        self.root2, textvariable=self.var_new_pass, font=('Lucida Calligraphy', 22))
                    self.nptext.place(x=60, y=320, width=300)

                    resetbtn = Button(self.root2, text='Reset Password', command=reset_password, font=('Lucida Calligraphy', 15, 'bold'), bd=3,
                                      relief=RIDGE, bg='green',
                                      fg='black', activeforeground='white', activebackground='red')
                    resetbtn.place(x=130, y=380, width=150, height=40)

        # ===============================================================================================

        self.bg = ImageTk.PhotoImage(file=r"images/bg.jpeg")
        f_lbl1 = Label(root, image=self.bg)
        f_lbl1.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        frame = Frame(root, bg='black')
        frame.place(x=660, y=170, width=380, height=580)

        # First image
        img = Image.open(r"images/login.png")
        img = img.resize((70, 70), Image.ANTIALIAS)
        self.ph = ImageTk.PhotoImage(img)

        f_lbl = Label(frame, image=self.ph, bg='black', borderwidth=0)
        f_lbl.place(x=158, y=35, width=70, height=70)

        # Text
        text = Label(frame, text='Login here', font=(
            'Lucida Calligraphy', 20, 'bold'), bg='black', fg='white')
        text.place(x=136, y=120)

        # Login Labels
        username = Label(frame, text='Username', font=(
            'Lucida Calligraphy', 15, 'bold'), bg='black', fg='white')
        username.place(x=70, y=190)
        usertext = ttk.Entry(frame, textvariable=self.var_email, font=(
            'Lucida Calligraphy', 15, 'bold'))
        usertext.place(x=50, y=230, width=300)

        password = Label(frame, text='Password', font=(
            'Lucida Calligraphy', 15, 'bold'), bg='black', fg='white')
        password.place(x=70, y=280)
        pwtext = ttk.Entry(frame, textvariable=self.var_pass,
                           font=('Lucida Calligraphy', 15, 'bold'))
        pwtext.place(x=50, y=310, width=300)

        # ======== Images ===========
        # Icons
        img3 = Image.open(r"images/login.png")
        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.ph3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(frame, image=self.ph3, bg='black', borderwidth=0)
        f_lbl.place(x=50, y=193, width=20, height=20)

        img4 = Image.open(r"images/passwordIc.png")
        img4 = img4.resize((20, 20), Image.ANTIALIAS)
        self.ph4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(frame, image=self.ph4, bg='black', borderwidth=0)
        f_lbl.place(x=50, y=283, width=20, height=20)

        # --------- Buttons ----------------------

        loginbtn = Button(frame, text='Login', command=login, font=('Lucida Calligraphy', 15, 'bold'), bd=3, relief=RIDGE, bg='red',
                          fg='white', activeforeground='white', activebackground='red')
        loginbtn.place(x=130, y=380, width=120, height=40)

        registerbtn = Button(frame, command=register_window, text='Sign Up', font=('Lucida Calligraphy', 10, 'bold'), borderwidth=0, bg='black',
                             fg='white')
        registerbtn.place(x=50, y=450, width=120)

        fgtbtn = Button(frame, text='Forgot password', command=forgot_password, font=(
            'Lucida Calligraphy', 10, 'bold'), fg='white', bg='black')
        fgtbtn.place(x=50, y=480, width=120)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Register')

        self.bg = ImageTk.PhotoImage(file=r"images/bag.jpeg")
        f_lbl1 = Label(root, image=self.bg)
        f_lbl1.place(x=0, y=0, relwidth=1, relheight=1)

        # ================================ Variables ====================================================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ===============================================================================================

        # ================================ Functions ====================================================
        def register_data():
            if self.var_fname.get() == '' or self.var_lname.get() == '' or self.var_contact.get() == '' or self.var_email.get() == '' or self.var_pass.get() == '' or self.var_confpass.get() == '':
                messagebox.showerror('Error', 'All fields are required')
            elif self.var_securityQ.get() == 'Select':
                messagebox.showerror(
                    'Error', 'Please select a security question!')
            elif self.var_securityA.get() == '':
                messagebox.showerror(
                    'Error', 'Answer the selected security question!')
            elif self.var_pass.get() != self.var_confpass.get():
                messagebox.showerror(
                    'Error', 'Passwords and Confirm Passwords must be same!')
                self.var_pass.set('')
                self.var_confpass.set('')
            elif self.var_check.get() == 0:
                messagebox.showerror(
                    'Error', 'Please Agree with the Terms and Conditions')
            else:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                query = 'SELECT * FROM register WHERE email=%s'
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror(
                        'Error', 'User already exists, please try another email')
                else:
                    my_cursor.execute('INSERT INTO register values (%s, %s, %s, %s, %s, %s, %s)', (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'User registered successfully!')

        def return_login():
            self.root.destroy()

        # ===============================================================================================

        # ----------- Main Frame ------------------------
        frame = Frame(root, bg='white')
        frame.place(x=425, y=170, width=850, height=600)

        # Register
        text = Label(frame, text='REGISTER HERE', font=(
            'Lucida Calligraphy', 28, 'bold'), bg='white', fg='darkgreen')
        text.place(x=320, y=10)

        # ----------- Label Entry ------------------------
        firstname = Label(frame, text='First Name', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        firstname.place(x=50, y=100)
        ftext = ttk.Entry(frame, textvariable=self.var_fname,
                          font=('Lucida Calligraphy', 22, 'bold'))
        ftext.place(x=50, y=140, width=300)

        lastname = Label(frame, text='Last Name', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        lastname.place(x=500, y=100)
        ltext = ttk.Entry(frame, textvariable=self.var_lname,
                          font=('Lucida Calligraphy', 22, 'bold'))
        ltext.place(x=500, y=140, width=300)

        contact = Label(frame, text='Phone Number', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        contact.place(x=50, y=190)
        ctext = ttk.Entry(frame, textvariable=self.var_contact,
                          font=('Lucida Calligraphy', 22, 'bold'))
        ctext.place(x=50, y=230, width=300)

        email = Label(frame, text='Email', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        email.place(x=500, y=190)
        etext = ttk.Entry(frame, textvariable=self.var_email,
                          font=('Lucida Calligraphy', 22, 'bold'))
        etext.place(x=500, y=230, width=300)

        question = Label(frame, text='Select Security Question', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        question.place(x=50, y=280)
        combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=('Lucida Calligraphy', 22, 'bold'),
                             state='readonly')
        combo['values'] = (
            'Select', 'Your birth place', 'Your favourite city', 'Your favourite car', 'Your bestfriend name')
        combo.place(x=50, y=320, width=300)
        combo.current(0)

        answer = Label(frame, text='Security Answer', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        answer.place(x=500, y=280)
        atext = ttk.Entry(frame, textvariable=self.var_securityA,
                          font=('Lucida Calligraphy', 22, 'bold'))
        atext.place(x=500, y=320, width=300)

        pw = Label(frame, text='Password', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        pw.place(x=50, y=360)
        ptext = ttk.Entry(frame, textvariable=self.var_pass,
                          font=('Lucida Calligraphy', 22, 'bold'))
        ptext.place(x=50, y=400, width=300)

        cpw = Label(frame, text='Confirm Password', font=(
            'Lucida Calligraphy', 22, 'bold'), bg='white')
        cpw.place(x=500, y=360)
        cptext = ttk.Entry(frame, textvariable=self.var_confpass,
                           font=('Lucida Calligraphy', 22, 'bold'))
        cptext.place(x=500, y=400, width=300)

        # ------------------- Check button ----------------------
        self.var_check = IntVar()
        check = Checkbutton(frame, variable=self.var_check, text='I agree with the Terms and Conditions',
                            font=('Lucida Calligraphy', 15, 'bold'), onvalue=1, offvalue=0)
        check.place(x=50, y=450)

        # ------------------- Button ----------------------------
        # Register
        img = Image.open(r"images/reg.png")
        img = img.resize((200, 50), Image.ANTIALIAS)
        self.ph = ImageTk.PhotoImage(img)

        r_lbl = Button(frame, image=self.ph, command=register_data,
                       borderwidth=0, cursor='hand2')
        r_lbl.place(x=100, y=490, width=200, height=50)

        # Login
        img1 = Image.open(r"images/loginnow.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.ph1 = ImageTk.PhotoImage(img1)

        f_lbl = Button(frame, image=self.ph1, command=return_login,
                       borderwidth=0, cursor='hand2')
        f_lbl.place(x=550, y=490, width=200, height=50)


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

        lbl = Label(title, font=('Lucida Calligraphy',
                    20, 'bold'), bg='white', fg='red')
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
            self.exit = tkinter.messagebox.askyesno(
                'Face Recognition', 'Are you sure you want to exit!?')
            if self.exit > 0:
                self.root.destroy()
            else:
                return
        # ================================================================================

        # Student link----->
        img4 = Image.open(r"images/students.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.ph4 = ImageTk.PhotoImage(img4)
        # Text
        b1 = Button(b_img, image=self.ph4,
                    command=student_details, cursor='hand2')
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
        b2 = Button(b_img, image=self.ph6,
                    command=attendance_data, cursor='hand2')
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


class Face_Recognition_System1:
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

        lbl = Label(title, font=('Lucida Calligraphy',
                    20, 'bold'), bg='white', fg='red')
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
            self.exit = tkinter.messagebox.askyesno(
                'Face Recognition', 'Are you sure you want to exit!?')
            if self.exit > 0:
                self.root.destroy()
            else:
                return
        # ================================================================================

        # Student link----->
        img4 = Image.open(r"images/students.png")
        img4 = img4.resize((320, 320), Image.ANTIALIAS)
        self.ph4 = ImageTk.PhotoImage(img4)
        # Text
        b1 = Button(b_img, image=self.ph4,
                    command=student_details, cursor='hand2')
        b1.place(x=150, y=100, width=320, height=320)

        b1_1 = Button(b_img, text='Student details', command=student_details, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b1_1.place(x=150, y=415, width=320, height=40)

        # Detect Face link----->
        img5 = Image.open(r"images/face.png")
        img5 = img5.resize((320, 320), Image.ANTIALIAS)
        self.ph5 = ImageTk.PhotoImage(img5)
        # Text
        b2 = Button(b_img, image=self.ph5, command=face_data, cursor='hand2')
        b2.place(x=700, y=100, width=320, height=320)

        b2_1 = Button(b_img, text='Face Detector', command=face_data, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=700, y=415, width=320, height=40)

        # Help Desk link----->
        img7 = Image.open(r"images/help.jpeg")
        img7 = img7.resize((320, 320), Image.ANTIALIAS)
        self.ph7 = ImageTk.PhotoImage(img7)
        # Text
        b2 = Button(b_img, image=self.ph7, command=help, cursor='hand2')
        b2.place(x=1250, y=100, width=320, height=320)

        b2_1 = Button(b_img, text='Help Desk', command=help, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=1250, y=415, width=320, height=40)

        # Developer link----->
        img10 = Image.open(r"images/dev.jpeg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.ph10 = ImageTk.PhotoImage(img10)
        # Text
        b2 = Button(b_img, image=self.ph10, command=developer, cursor='hand2')
        b2.place(x=475, y=475, width=220, height=220)

        b2_1 = Button(b_img, text='Developer', command=developer, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=475, y=675, width=220, height=40)

        # Exit link----->
        img11 = Image.open(r"images/exit.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.ph11 = ImageTk.PhotoImage(img11)
        # Text
        b2 = Button(b_img, image=self.ph11, command=exit, cursor='hand2')
        b2.place(x=1025, y=475, width=220, height=220)

        b2_1 = Button(b_img, text='Exit', command=exit, cursor='hand2',
                      font=('lucida calligraphy', 14, 'bold'), bg='white', fg='black')
        b2_1.place(x=1025, y=675, width=220, height=40)


if __name__ == '__main__':
    main()
