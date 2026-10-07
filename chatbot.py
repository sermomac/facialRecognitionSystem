from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("750x620")
        self.root.bind('<Return>')

        # Main Frame
        main_frame = Frame(root, bd=3,bg='powder blue')
        main_frame.place(x=0, y=0, width=750)

        img_chat = Image.open(r"images/chatIcon.jpg")
        img_chat = img_chat.resize((200, 70), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730, image=self.photoimg,
                            text='CHAT WITH ME', font=('times new roman', 30, 'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=('times new roman', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()


if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
