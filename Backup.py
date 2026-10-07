from tkinter import *
from tkinter import messagebox
from books import Books
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry('2560x1600')
        self.root.title("Library Management with face recognition")




if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

