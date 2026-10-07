from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title('Face Recognition System')

        # =================== Functions ==========================
        def train_classifier():
            data_dir = "data"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            for image in path:
                img = Image.open(image).convert('L')  # Gray scale image
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1) == 13
            ids = np.array(ids)

            # ------------ Train the classifier and save ---------------------
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write('classifier.xml')
            cv2.destroyAllWindows()
            messagebox.showinfo('Result', 'Training Data Set Completed!')
        # ===========================================================
        # Title
        title = Label(self.root, text='TRAIN DATA SET',
                      font=('Lucida Calligraphy', 28, 'bold'),
                      bg='white', fg='red')
        title.place(x=0, y=0, width=1700, height=45)

        # Images top
        top_img = Image.open(r"images/dataset.jpeg")
        top_img = top_img.resize((1700, 525), Image.ANTIALIAS)
        self.ph_top = ImageTk.PhotoImage(top_img)

        img1 = Label(self.root, image=self.ph_top)
        img1.place(x=0, y=45, width=1700, height=525)

        # Button
        b1_1 = Button(self.root, text='TRAIN DATA', command=train_classifier, cursor='hand2',
                      font=('lucida calligraphy', 20, 'bold'), bg='white', fg='black')
        b1_1.place(x=0, y=440, width=1700, height=60)

        # Images bottom
        b_img = Image.open(r"images/datas.jpeg")
        b_img = b_img.resize((1700, 425), Image.ANTIALIAS)
        self.ph_b = ImageTk.PhotoImage(b_img)

        img2 = Label(self.root, image=self.ph_b)
        img2.place(x=0, y=500, width=1700, height=425)


if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()
