from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # =========== Variables =======================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # ======================== function declaration ================================================================
        # -----------------Insert data -----------------------------
        def add_data():
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get()
                        ))
                    conn.commit()
                    fecth_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

        # ---------------- Fetch data ------------------------
        def fecth_data():
            conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                           database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert('', END, values=i)
                conn.commit()
                conn.close()

        # ------------- get cursor --------------------------------
        def get_cursor(event=''):
            cursor_focus = self.student_table.focus()
            content = self.student_table.item(cursor_focus)
            data = content['values']

            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.var_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])

        # ------------- Update data --------------------
        def update_data():
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
            else:
                try:
                    Update = messagebox.askyesno("Update", "Do you want to update the student details?",
                                                 parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                                       database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute(
                            "UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                            (
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_std_id.get()
                            ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success", "Student details updated successfully!", parent=self.root)
                    conn.commit()
                    fecth_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

        # ----------- Delete data ----------------------
        def delete_data():
            if self.var_std_id.get() == "":
                messagebox.showerror("Error", "Student ID is required!", parent=self.root)
            else:
                try:
                    Delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?",
                                                 parent=self.root)
                    if Delete > 0:
                        conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                                       database="face_recognizer")
                        my_cursor = conn.cursor()
                        sql = "DELETE FROM student WHERE Student_id=%s"
                        val = (self.var_std_id.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not Delete:
                            return
                    conn.commit()
                    fecth_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Student details deleted successfully!", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

        # ------------- Reset data ------------------------
        def reset_data():
            self.var_dep.set('Select Department')
            self.var_course.set('Select Course')
            self.var_year.set('Select Year')
            self.var_semester.set('Select Semester')
            self.var_std_id.set('')
            self.var_std_name.set('')
            self.var_div.set('Select Division')
            self.var_roll.set('')
            self.var_gender.set('Male')
            self.var_dob.set('')
            self.var_email.set('')
            self.var_phone.set('')
            self.var_address.set('')
            self.var_teacher.set('')
            self.var_radio1.set('')

        # ---------------- Generate data take photo sample --------------
        def generate_dataset():
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute('SELECT * FROM student')
                    my_result = my_cursor.fetchall()
                    id = 0
                    for x in my_result:
                        id += 1
                    my_cursor.execute(
                        "UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get() == id + 1
                        ))
                    conn.commit()
                    fecth_data()
                    reset_data()
                    conn.close()
                    # ------------ Load pre defined data for open CV------------------
                    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # ---------------------Scaling factor = 1.3
                        # ---------------------Minimum neighbour = 5

                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    cap.set(3, 640)
                    cap.set(4, 480)
                    cap.set(10, 100)
                    cv2.namedWindow('Photo Sample')
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                        # face = cv2.resize(face_cropped(my_frame), (450, 450), interpolation= cv2.INTER_LINEAR)
                        face = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow('Cropped Face', face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo('Result', 'Data Set Generated Successfully!')

                except Exception as es:
                    messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

        # ==============================================================================================================

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
        title = Label(b_img, text='STUDENT MANAGEMENT SYSTEM',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Main Frame
        main_frame = Frame(b_img, bd=2, bg='white')
        main_frame.place(x=20, y=50, width=1650, height=700)

        # Left side label frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Details',
                                font=('Lucida Calligraphy', 12, 'bold'))
        left_frame.place(x=10, y=10, width=820, height=670)

        lft_img = Image.open(r"images/1.jpeg")
        lft_img = lft_img.resize((800, 130), Image.ANTIALIAS)
        self.ph_left = ImageTk.PhotoImage(lft_img)

        img1 = Label(left_frame, image=self.ph_left)
        img1.place(x=10, y=0, width=800, height=130)

        # Current course
        current_course = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Current Course Information',
                                    font=('Lucida Calligraphy', 12, 'bold'))
        current_course.place(x=5, y=135, width=805, height=120)

        # Department
        dep = Label(current_course, text='Department', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=0, column=0, padx=10, sticky=W)

        # var = StringVar()
        # var.set('Select option')
        # d_drop = OptionMenu(current_course, var, 'MCA', 'MBA', 'Msc', 'M Tech')
        # d_drop.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # Or I could use a combo box--------------------------------------------------------------->
        d_combo = ttk.Combobox(current_course, textvariable=self.var_dep, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Select Department', 'MCA', 'MBA', 'Msc', 'M Tech', 'MA')
        d_combo.current(0)
        d_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # ----------------------------------------------------------------------------------------->

        # Course
        dep = Label(current_course, text='Course', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=0, column=3, padx=10, sticky=W)

        # var = StringVar()
        # var.set('Select option')
        # d_drop = OptionMenu(current_course, var, 'MCA', 'MBA', 'Msc', 'M Tech')
        # d_drop.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_course, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Select Course', 'MCA', 'MBA', 'Msc', 'M Tech', 'MA')
        d_combo.current(0)
        d_combo.grid(row=0, column=4, padx=2, pady=10, sticky=W)

        # Year
        dep = Label(current_course, text='Year', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=1, column=0, padx=10, sticky=W)

        # var = StringVar()
        # var.set('Select option')
        # d_drop = OptionMenu(current_course, var, 'I Year', 'II Year', 'III Year', 'IV Year')
        # d_drop.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_year, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Select Year', 'I Year', 'II Year', 'III Year', 'IV Year')
        d_combo.current(0)
        d_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        dep = Label(current_course, text='Semester', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=1, column=3, padx=10, sticky=W)

        # var = StringVar()
        # var.set('Select option')
        # d_drop = OptionMenu(current_course, var, 'Fisrt', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth')
        # d_drop.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        d_combo = ttk.Combobox(current_course, textvariable=self.var_semester, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Select Semester', 'Fisrt', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth')
        d_combo.current(0)
        d_combo.grid(row=1, column=4, padx=2, pady=10, sticky=W)

        # Class Student Information
        student = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Class Student Information',
                             font=('Lucida Calligraphy', 12, 'bold'))
        student.place(x=5, y=260, width=805, height=380)

        # ID
        s_id = Label(student, text='Student ID', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_std_id, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        s_id = Label(student, text='Student Name', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_std_name, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Class division
        s_id = Label(student, text='Class Division', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        d_combo = ttk.Combobox(student, textvariable=self.var_div, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Select Division', 'A', 'B', 'C')
        d_combo.current(0)
        d_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Roll No
        s_id = Label(student, text='Roll No', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_roll, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Gender
        s_id = Label(student, text='Gender', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        d_combo = ttk.Combobox(student, textvariable=self.var_gender, font=('Lucida Calligraphy', 12, 'bold'),
                               state='readonly')
        d_combo['values'] = ('Male', 'Female', 'Other')
        d_combo.current(0)
        d_combo.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # DOB
        s_id = Label(student, text='Date of Birth', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_dob, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Email
        s_id = Label(student, text='Email', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_email, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Phone number
        s_id = Label(student, text='Phone No', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_phone, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=3, column=3, padx=10, pady=10, sticky=W)

        # Address
        s_id = Label(student, text='Address', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_address, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        # Teacher name
        s_id = Label(student, text='Teacher Name', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=4, column=2, padx=10, pady=10, sticky=W)
        s_entry = ttk.Entry(student, textvariable=self.var_teacher, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=4, column=3, padx=10, pady=10, sticky=W)

        # Radio buttons
        self.var_radio1 = StringVar()
        radio_btn = Radiobutton(student, command=generate_dataset, variable=self.var_radio1, text='Take photo sample',
                                value='Yes')
        radio_btn.grid(row=6, column=0, padx=10, pady=10, sticky=W)

        radio_btn1 = Radiobutton(student, variable=self.var_radio1, text='No photo sample', value='No')
        radio_btn1.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        # Buttons frame
        btn_frame = Frame(student, bd=2, relief=RIDGE)
        btn_frame.place(x=35, y=295, width=670, height=24)

        save_btn = Button(btn_frame, text='Save', width=18, command=add_data, font=('Lucida Calligraphy', 12, 'bold'),
                          bg='blue',
                          fg='black')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text='Update', width=18, command=update_data,
                            font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Delete', width=18, command=delete_data,
                            font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', width=18, command=reset_data,
                           font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                           fg='black')
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(student, bd=2, relief=RIDGE)
        btn_frame1.place(x=38, y=325, width=663, height=24)

        photo_btn = Button(btn_frame1, text='Take photo', width=36, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                           fg='black')
        photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text='Update photo', width=36, font=('Lucida Calligraphy', 12, 'bold'),
                                  bg='blue',
                                  fg='black')
        update_photo_btn.grid(row=1, column=1)

        # Right side label frame---------------------------------------------------------->
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Details',
                                 font=('Lucida Calligraphy', 12, 'bold'))
        # right_frame.place(x=840, y=10, width=800, height=670)

        r_img = Image.open(r"images/1.jpeg")
        r_img = r_img.resize((780, 130), Image.ANTIALIAS)
        self.ph_r = ImageTk.PhotoImage(r_img)

        f_lblr = Label(right_frame, image=self.ph_r)
        f_lblr.place(x=10, y=0, width=780, height=130)

        # Search system ------------------------------------------------------------------------->
        search = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE, text='Search System',
                            font=('Lucida Calligraphy', 12, 'bold'))
        search.place(x=10, y=135, width=780, height=65)

        # Search label
        search_lbl = Label(search, text='Search by', font=('Lucida Calligraphy', 12, 'bold'))
        search_lbl.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        # Search dropdown
        var = StringVar()
        var.set('Select option')
        search_menu = OptionMenu(search, var, 'Student ID', 'Phone number')
        search_menu.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Entry
        search_entry = ttk.Entry(search, width=16, font=('Lucida Calligraphy', 12))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Search buttons
        search_btn = Button(search, text='Search', width=14, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        search_btn.grid(row=0, column=3)

        show_all_btn = Button(search, text='Show all', width=14, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                              fg='black')
        show_all_btn.grid(row=0, column=4)

        # Table------------------------------------------------------------------------------------>
        table_frame = Frame(right_frame, bg='white', relief=RIDGE)
        table_frame.place(x=10, y=200, width=780, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            'Dep', 'Course', 'Year', 'Sem', 'ID', 'Name', 'Div', 'Roll', 'Gender', 'DOB', 'Email', 'PhoneNumber',
            'Teacher',
            'Photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Dep', text='Department')
        self.student_table.heading('Course', text='Course')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('Sem', text='Semester')
        self.student_table.heading('ID', text='ID')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Div', text='Division')
        self.student_table.heading('Roll', text='Roll')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('DOB', text='Date of birth')
        self.student_table.heading('Email', text='E-mail')
        self.student_table.heading('PhoneNumber', text='Phone number')
        self.student_table.heading('Teacher', text='Teacher')
        self.student_table.heading('Photo', text='Photo Sample Status')
        self.student_table['show'] = 'headings'

        self.student_table.column('Dep', width=100)
        self.student_table.column('Course', width=100)
        self.student_table.column('Year', width=100)
        self.student_table.column('Sem', width=100)
        self.student_table.column('ID', width=100)
        self.student_table.column('Name', width=100)
        self.student_table.column('Div', width=100)
        self.student_table.column('Roll', width=100)
        self.student_table.column('Gender', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('Email', width=100)
        self.student_table.column('PhoneNumber', width=100)
        self.student_table.column('Teacher', width=100)
        self.student_table.column('Photo', width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", get_cursor)
        fecth_data()


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
