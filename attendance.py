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

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # =========== Variables =======================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()


        # ================================ Functions ====================================================
        def fetch_data(rows):
            AttendanceReportTable.delete(*AttendanceReportTable.get_children())
            for i in rows:
                AttendanceReportTable.insert("", END, values=i)

        def importCSV():
            global myData
            myData.clear()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File', '*csv'), ('All Files', '*.*')), parent=root)
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=',')
                for i in csvread:
                    myData.append(i)
                fetch_data(myData)


        def exportCSV():
            try:
                if len(myData) < 1:
                    messagebox.showerror('No Data', 'No Data Found to export', parent=root)
                    return False
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File', '*csv'), ('All Files', '*.*')), parent=root)
                with open(fln, mode='w', newline='') as myfile:
                    exp_write = csv.writer(myfile, delimiter=',')
                    for i in myData:
                        exp_write.writerow(i)
                    messagebox.showinfo('Data Export', 'Data exported to '+os.path.basename(fln)+ '  successfully!')

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


        def get_cursor(event=''):
            cursor_row = AttendanceReportTable.focus()
            content = AttendanceReportTable.item(cursor_row)
            rows = content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

        def update_data():
            try:
                if len(myData) < 1:
                    messagebox.showerror('No Data', 'No Data Found to export', parent=root)
                    return False
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Open CSV', filetypes=(('CSV File', '*csv'), ('All Files', '*.*')), parent=root)
                with open(fln, mode='a', newline='') as myfile:
                    exp_write = csv.writer(myfile, delimiter=',')
                    for i in myData:
                        exp_write.writerow(i)
                    messagebox.showinfo('Data Export', 'Data updated in '+os.path.basename(fln)+ '  successfully!')

            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


        def reset_data():
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set('Status')


        # ==============================================================================================================

        # Header images
        # First image
        img = Image.open(r"images/facial.jpeg")
        img = img.resize((840, 200), Image.ANTIALIAS)
        self.ph = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.ph)
        f_lbl.place(x=0, y=0, width=840, height=200)

        # Second image
        img1 = Image.open(r"images/1.jpeg")
        img1 = img1.resize((840, 200), Image.ANTIALIAS)
        self.ph1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.ph1)
        f_lbl1.place(x=840, y=0, width=840, height=200)


        # Background image
        img3 = Image.open(r"images/2.jpeg")
        img3 = img3.resize((1700, 800), Image.ANTIALIAS)
        self.ph3 = ImageTk.PhotoImage(img3)

        b_img = Label(self.root, image=self.ph3)
        b_img.place(x=0, y=130, width=1700, height=800)

        # Title
        title = Label(b_img, text='ATTENDANCE MANAGEMENT SYSTEM',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Main Frame
        main_frame = Frame(b_img, bd=2, bg='white')
        main_frame.place(x=20, y=50, width=1650, height=730)

        # Left side label frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Student Attendance',
                                font=('Lucida Calligraphy', 12, 'bold'))
        left_frame.place(x=10, y=10, width=820, height=690)

        lft_img = Image.open(r"images/1.jpeg")
        lft_img = lft_img.resize((800, 130), Image.ANTIALIAS)
        self.ph_left = ImageTk.PhotoImage(lft_img)

        img1 = Label(left_frame, image=self.ph_left)
        img1.place(x=10, y=0, width=800, height=130)

        # Left side inner label frame
        left_inner_frame = Frame(left_frame, bd=2, bg='white', relief=RIDGE)
        left_inner_frame.place(x=10, y=140, width=800, height=520)

        # Label frame
        label_frame = Frame(left_inner_frame, bd=2, bg='white', relief=RIDGE)
        label_frame.place(x=40, y=120, width=700, height=180)

        # ------------------- Label and Entry ------------------------
        # Attendance ID
        AttendanceID = Label(label_frame, text='Attendance ID:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_id, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        AttendanceID = Label(label_frame, text='Name:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_name, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Time
        AttendanceID = Label(label_frame, text='Time:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_time, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Roll
        AttendanceID = Label(label_frame, text='Roll No:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_roll, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        # Department
        AttendanceID = Label(label_frame, text='Department:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_dep, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Date
        AttendanceID = Label(label_frame, text='Date:', font=('Lucida Calligraphy', 12, 'bold'))
        AttendanceID.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        AttendanceID_Entry = ttk.Entry(label_frame, textvariable=self.var_atten_date, width=20, font=('Lucida Calligraphy', 12))
        AttendanceID_Entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        # Attendance
        status = Label(label_frame, text='Attendance Status:', font=('Lucida Calligraphy', 12, 'bold'))
        status.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        attend_status = ttk.Combobox(label_frame, textvariable=self.var_atten_attendance, width=20,  state='readonly', font=('Lucida Calligraphy', 12, 'bold'))
        attend_status['values'] = ('Status', 'Present', 'Absent')
        attend_status.grid(row=3, column=1, pady=8)
        attend_status.current(0)

        # Buttons frame
        btn_frame = Frame(left_inner_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=50, y=400, width=670, height=24)

        imp_btn = Button(btn_frame, text='Import CSV', width=18, command=importCSV, font=('Lucida Calligraphy', 12, 'bold'),
                          bg='blue',
                          fg='black')
        imp_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text='Export CSV', width=18, command=exportCSV,
                            font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text='Update CSV', width=18, command=update_data,
                            font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                            fg='black')
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', width=18, command=reset_data,
                           font=('Lucida Calligraphy', 12, 'bold'), bg='blue',
                           fg='black')
        reset_btn.grid(row=0, column=3)


        # Right side label frame---------------------------------------------------------->
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text='Attendance Details',
                                 font=('Lucida Calligraphy', 12, 'bold'))
        right_frame.place(x=840, y=10, width=800, height=690)

        # Right side inner label frame
        table_frame = Frame(right_frame, bd=2, bg='white', relief=RIDGE)
        table_frame.place(x=10, y=10, width=780, height=650)

        # Scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        AttendanceReportTable = ttk.Treeview(table_frame, columns=('ID', 'Roll', 'Name', 'Department', 'Time', 'Date', 'Attendance'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=AttendanceReportTable.xview)
        scroll_y.config(command=AttendanceReportTable.yview)

        AttendanceReportTable.heading('ID', text="Attendance ID")
        AttendanceReportTable.heading('Roll', text="Roll No")
        AttendanceReportTable.heading('Name', text="Name")
        AttendanceReportTable.heading('Department', text="Department")
        AttendanceReportTable.heading('Time', text="Time")
        AttendanceReportTable.heading('Date', text="Date")
        AttendanceReportTable.heading('Attendance', text="Attendance")

        AttendanceReportTable['show'] = 'headings'
        AttendanceReportTable.column('ID', width=100)
        AttendanceReportTable.column('Roll', width=100)
        AttendanceReportTable.column('Name', width=100)
        AttendanceReportTable.column('Department', width=100)
        AttendanceReportTable.column('Time', width=100)
        AttendanceReportTable.column('Date', width=100)
        AttendanceReportTable.column('Attendance', width=100)
        AttendanceReportTable.pack(fill=BOTH, expand=1)

        AttendanceReportTable.bind('<ButtonRelease>', get_cursor)


if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
