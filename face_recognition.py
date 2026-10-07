from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # =================== Functions ==========================
        def face_recog():
            def draw_boundray(img, classifier, scaleFactor,  minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confindence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="macarringue",
                                                   database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Student_id from student WHERE Student_id=" + str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i)

                    my_cursor.execute("SELECT Name from student WHERE Student_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)

                    my_cursor.execute("SELECT Roll from student WHERE Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("SELECT Department from student WHERE Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    if confindence > 77:
                        cv2.putText(img, f"Student ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        mark_attendance(i, r, n, d)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, f"Unknown Face!", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]
                return coord

            def recognize(img, clf, faceCascade):
                coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
                return img

            faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read(r'classifier.xml')

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()


        # ===================== Attendance ==========================
        def mark_attendance(i, r, n, d):
            with open('Sergio.csv', 'r+', newline='\n') as f:
                myDataList = f.readline()
                name_list = []
                for line in myDataList:
                    entry = line.split((','))
                    name_list.append(entry)
                if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now = datetime.now()
                    d1 = now.strftime('%d/%m/%Y')
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        # ===========================================================

        # Title
        title = Label(self.root, text='FACE RECOGNITION',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Images Left
        top_img = Image.open(r"images/face.jpeg")
        top_img = top_img.resize((900, 1000), Image.ANTIALIAS)
        self.ph_top = ImageTk.PhotoImage(top_img)

        img1 = Label(self.root, image=self.ph_top)
        img1.place(x=0, y=55, width=900, height=1000)

        # Images Right
        r_img = Image.open(r"images/face_rec.jpeg")
        r_img = r_img.resize((950, 1000), Image.ANTIALIAS)
        self.r_top = ImageTk.PhotoImage(r_img)

        img2 = Label(self.root, image=self.r_top)
        img2.place(x=800, y=55, width=950, height=1000)

        # Button
        b1_1 = Button(img2, text='FACE RECOGNITION', command=face_recog, cursor='hand2',
                      font=('lucida calligraphy', 20, 'bold'), bg='white', fg='black')
        b1_1.place(x=350, y=780, width=200, height=40)


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
