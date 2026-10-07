from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk


class Books:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title("Book details")

        # Header images
        # First image
        img = Image.open(r"images/facial.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.ph = ImageTk.PhotoImage(img)

        img1 = Label(self.root, image=self.ph)
        img1.place(x=0, y=0, width=500, height=130)

        # Second image
        img = Image.open(r"images/1.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.ph1 = ImageTk.PhotoImage(img)

        img1 = Label(self.root, image=self.ph1)
        img1.place(x=500, y=0, width=500, height=130)

        # Third image
        img = Image.open(r"images/4.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.ph2 = ImageTk.PhotoImage(img)

        img1 = Label(self.root, image=self.ph2)
        img1.place(x=1000, y=0, width=500, height=130)

        # Background image
        img = Image.open(r"images/2.jpeg")
        img = img.resize((1500, 710), Image.ANTIALIAS)
        self.ph3 = ImageTk.PhotoImage(img)

        img1 = Label(self.root, image=self.ph3)
        img1.place(x=0, y=130, width=1500, height=710)

        # Title
        title = Label(img1, text='LIBRARY MANAGEMENT SYSTEM', font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1500, height=45)

        main_frame = Frame(img1, bd=2, bg='white')
        main_frame.place(x=20, y=50, width=1405, height=590)

        # Left side label frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Book details',
                                font=('Lucida Calligraphy', 12, 'bold'))
        left_frame.place(x=10, y=10, width=720, height=570)

        lft_img = Image.open(r"images/1.jpeg")
        lft_img = lft_img.resize((700, 130), Image.ANTIALIAS)
        self.ph_left = ImageTk.PhotoImage(lft_img)

        img1 = Label(left_frame, image=self.ph_left)
        img1.place(x=10, y=0, width=700, height=130)

        # Details
        details = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Book information',
                             font=('Lucida Calligraphy', 12, 'bold'))
        details.place(x=5, y=135, width=705, height=120)

        # Department
        dep = Label(details, text='Department', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=0, column=0, padx=10, sticky=W)

        var = StringVar()
        var.set('Select option')
        d_drop = OptionMenu(details, var, 'MCA', 'MBA', 'Msc', 'M Tech')
        d_drop.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Or I could use a combo box--------------------------------------------------------------->
        # d_combo = ttk.Combobox(details, font=('Lucida Calligraphy', 12, 'bold'), state='readonly')
        # d_combo['values']=('Select department', 'IT', 'MCA')
        # d_combo.current(0)
        # d_combo.grid(row=0, column=1)
        # ----------------------------------------------------------------------------------------->

        # Course
        dep = Label(details, text='Course', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=0, column=2, padx=10, sticky=W)

        var = StringVar()
        var.set('Select option')
        d_drop = OptionMenu(details, var, 'MCA', 'MBA', 'Msc', 'M Tech')
        d_drop.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        dep = Label(details, text='Year', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=1, column=0, padx=10, sticky=W)

        var = StringVar()
        var.set('Select option')
        d_drop = OptionMenu(details, var, 'I Year', 'II Year', 'III Year', 'IV Year')
        d_drop.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        dep = Label(details, text='Semester', font=('Lucida Calligraphy', 12, 'bold'))
        dep.grid(row=1, column=2, padx=10, sticky=W)

        var = StringVar()
        var.set('Select option')
        d_drop = OptionMenu(details, var, 'Fisrt', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth')
        d_drop.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student information
        student = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text='Student information',
                             font=('Lucida Calligraphy', 12, 'bold'))
        student.place(x=5, y=260, width=705, height=280)

        # ID
        s_id = Label(student, text='Student Id', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        s_id = Label(student, text='Student Name', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division
        s_id = Label(student, text='Class Division', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        s_id = Label(student, text='Roll No', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        s_id = Label(student, text='Gender', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        s_id = Label(student, text='Date of Birth', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        s_id = Label(student, text='Email', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone number
        s_id = Label(student, text='Phone No', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        s_id = Label(student, text='Address', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        s_id = Label(student, text='Teacher Name', font=('Lucida Calligraphy', 12, 'bold'))
        s_id.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        s_entry = ttk.Entry(student, width=20, font=('Lucida Calligraphy', 12))
        s_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons
        radio_btn = Radiobutton(student, text='Take photo sample', value='Yes')
        radio_btn.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        radio_btn1 = Radiobutton(student, text='No photo sample', value='Yes')
        radio_btn1.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Buttons frame
        btn_frame = Frame(student, bd=2, relief=RIDGE)
        btn_frame.place(x=15, y=205, width=670, height=24)

        save_btn = Button(btn_frame, text='Save', width=18, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                          fg='black')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text='Update', width=18, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Delete', width=18, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', width=18, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                           fg='black')
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(student, bd=2, relief=RIDGE)
        btn_frame1.place(x=18, y=235, width=663, height=24)

        photo_btn = Button(btn_frame1, text='Take photo', width=36, font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                           fg='black')
        photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text='Update photo', width=36, font=('Lucida Calligraphy', 12, 'bold'),
                                  bg='blue',
                                  fg='black')
        update_photo_btn.grid(row=1, column=1)

        # Right side label frame---------------------------------------------------------->
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Book details',
                                 font=('Lucida Calligraphy', 12, 'bold'))
        right_frame.place(x=740, y=10, width=650, height=570)

        rgt_img = Image.open(r"images/1.jpeg")
        rgt_img = lft_img.resize((700, 130), Image.ANTIALIAS)
        ph_rgt = ImageTk.PhotoImage(rgt_img)

        img2 = Label(right_frame, image=ph_rgt)
        img2.place(x=10, y=0, width=700, height=130)

        # Search system ------------------------------------------------------------------------->
        search = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE, text='Search System',
                            font=('Lucida Calligraphy', 12, 'bold'))
        search.place(x=5, y=135, width=635, height=65)

        # Search label
        search_lbl = Label(search, text='Search by', font=('Lucida Calligraphy', 12, 'bold'))
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Search dropdown
        var = StringVar()
        var.set('Select option')
        search_menu = OptionMenu(search, var, 'Roll number', 'Phone number')
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
        table_frame.place(x=10, y=200, width=635, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        student_table = ttk.Treeview(table_frame, columns=(
            'Dep', 'Course', 'Year', 'Sem', 'ID', 'Name', 'Div', 'Roll', 'Gender', 'DOB', 'Email', 'PhoneNumber',
            'Teacher',
            'Photo'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)

        student_table.heading('Dep', text='Department')
        student_table.heading('Course', text='Course')
        student_table.heading('Year', text='Year')
        student_table.heading('Sem', text='Semester')
        student_table.heading('ID', text='ID')
        student_table.heading('Name', text='Name')
        student_table.heading('Div', text='Division')
        student_table.heading('Roll', text='Roll')
        student_table.heading('Gender', text='Gender')
        student_table.heading('DOB', text='Date of birth')
        student_table.heading('Email', text='E-mail')
        student_table.heading('PhoneNumber', text='Phone number')
        student_table.heading('Teacher', text='Teacher')
        student_table.heading('Photo', text='Photo Sample Status')
        student_table['show'] = 'headings'

        student_table.column('Dep', width=100)
        student_table.column('Course', width=100)
        student_table.column('Year', width=100)
        student_table.column('Sem', width=100)
        student_table.column('ID', width=100)
        student_table.column('Name', width=100)
        student_table.column('Div', width=100)
        student_table.column('Roll', width=100)
        student_table.column('Gender', width=100)
        student_table.column('DOB', width=100)
        student_table.column('Email', width=100)
        student_table.column('PhoneNumber', width=100)
        student_table.column('Teacher', width=100)
        student_table.column('Photo', width=150)

        student_table.pack(fill=BOTH, expand=1)


if __name__ == '__main__':
    root = Tk()
    obj = Books(root)
    root.mainloop()
