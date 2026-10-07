from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkmacosx import Button
from tkinter import messagebox
import mysql.connector


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
                messagebox.showerror('Error', 'Please select a security question!')
            elif self.var_securityA.get() == '':
                messagebox.showerror('Error', 'Answer the selected security question!')
            elif self.var_pass.get() != self.var_confpass.get():
                messagebox.showerror('Error', 'Passwords and Confirm Passwords must be same!')
                self.var_pass.set('')
                self.var_confpass.set('')
            elif self.var_check.get() == 0:
                messagebox.showerror('Error', 'Please Agree with the Terms and Conditions')
            else:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                query = 'SELECT * FROM register WHERE email=%s'
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror('Error', 'User already exists, please try another email')
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

        # ===============================================================================================

        # ----------- Main Frame ------------------------
        frame = Frame(root, bg='white')
        frame.place(x=425, y=170, width=850, height=600)

        # Register
        text = Label(frame, text='REGISTER HERE', font=('Lucida Calligraphy', 28, 'bold'), bg='white', fg='darkgreen')
        text.place(x=320, y=10)

        # ----------- Label Entry ------------------------
        firstname = Label(frame, text='First Name', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        firstname.place(x=50, y=100)
        ftext = ttk.Entry(frame, textvariable=self.var_fname, font=('Lucida Calligraphy', 22, 'bold'))
        ftext.place(x=50, y=140, width=300)

        lastname = Label(frame, text='Last Name', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        lastname.place(x=500, y=100)
        ltext = ttk.Entry(frame, textvariable=self.var_lname, font=('Lucida Calligraphy', 22, 'bold'))
        ltext.place(x=500, y=140, width=300)

        contact = Label(frame, text='Phone Number', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        contact.place(x=50, y=190)
        ctext = ttk.Entry(frame, textvariable=self.var_contact, font=('Lucida Calligraphy', 22, 'bold'))
        ctext.place(x=50, y=230, width=300)

        email = Label(frame, text='Email', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        email.place(x=500, y=190)
        etext = ttk.Entry(frame, textvariable=self.var_email, font=('Lucida Calligraphy', 22, 'bold'))
        etext.place(x=500, y=230, width=300)

        question = Label(frame, text='Select Security Question', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        question.place(x=50, y=280)
        combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=('Lucida Calligraphy', 22, 'bold'),
                             state='readonly')
        combo['values'] = (
        'Select', 'Your birth place', 'Your favourite city', 'Your favourite car', 'Your bestfriend name')
        combo.place(x=50, y=320, width=300)
        combo.current(0)

        answer = Label(frame, text='Security Answer', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        answer.place(x=500, y=280)
        atext = ttk.Entry(frame, textvariable=self.var_securityA, font=('Lucida Calligraphy', 22, 'bold'))
        atext.place(x=500, y=320, width=300)

        pw = Label(frame, text='Password', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        pw.place(x=50, y=360)
        ptext = ttk.Entry(frame, textvariable=self.var_pass, font=('Lucida Calligraphy', 22, 'bold'))
        ptext.place(x=50, y=400, width=300)

        cpw = Label(frame, text='Confirm Password', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        cpw.place(x=500, y=360)
        cptext = ttk.Entry(frame, textvariable=self.var_confpass, font=('Lucida Calligraphy', 22, 'bold'))
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

        r_lbl = Button(frame, image=self.ph, command=register_data, borderwidth=0, cursor='hand2')
        r_lbl.place(x=100, y=490, width=200, height=50)

        # Login
        img1 = Image.open(r"images/loginnow.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.ph1 = ImageTk.PhotoImage(img1)

        f_lbl = Button(frame, image=self.ph1, borderwidth=0, cursor='hand2')
        f_lbl.place(x=550, y=490, width=200, height=50)


if __name__ == '__main__':
    root = Tk()
    obj = Register(root)
    root.mainloop()
