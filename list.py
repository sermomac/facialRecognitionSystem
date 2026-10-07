from tkinter import *
from tkinter import messagebox
from books import Books
from PIL import Image, ImageTk


class List:
    def __init__(self, root):
        self.root = root
        self.root.geometry('560x600')
        self.root.title("Scan")

        list = [1, 6, 3, 5, 3, 4]
        list1 = [1, 6, 3, 5, 3, 4]

        def check_this():
            string = input("Enter string:")
            count1 = 0
            count2 = 0
            for i in string:
                if (i.islower()):
                    count1 = count1 + 1
                elif (i.isupper()):
                    count2 = count2 + 1
            print("The number of lowercase characters is:")
            print(count1)
            print("The number of uppercase characters is:")
            print(count2)

        def check():
            for i in list:
                if i.upper():
                    print('Upper')
                elif i.lower():
                    print('Upper')
                else:
                    pass

        Text = Label(root, text='Enter your text here:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        Text.place(x=50, y=100)
        ftext = Entry(root, font=('Lucida Calligraphy', 22))
        ftext.place(x=50, y=140, width=300)

        # Output
        output = Label(root, text='Output:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        output.place(x=50, y=200)

        # U
        U = Label(root, text='Number of U:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        U.place(x=50, y=250)
        UT = Label(root, text='Total Number of U:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        UT.place(x=50, y=350)
        # _
        l = Label(root, text='Number of _:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        l.place(x=50, y=300)

        lt = Label(root, text='Total Number of _:', font=('Lucida Calligraphy', 22, 'bold'), bg='white')
        lt.place(x=50, y=400)

        # Button
        Button(text='Scan', font=('Lucida Calligraphy', 22, 'bold'), borderwidth=0, command=check_this, cursor='hand2').place(x=150, y=450)


if __name__ == '__main__':
    root = Tk()
    obj = List(root)
    root.mainloop()
