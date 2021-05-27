from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk, Image

py = sys.executable


# creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.title("COURSE MANAGEMENT STUDENT LOGIN ")

        self.image = Image.open("mainbg.jpg")
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

        # verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD.")
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD.")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='test',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()
                    stud_id = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `student` where stud_id= %s AND password = %s ',
                                   (stud_id, password,))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'student_main.py'))
                    else:
                        print(pc)
                        messagebox.showinfo('Error.', 'Invalid username or password')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error.', "Something Went Wrong,Try Restarting.")

        def check():

            self.label = Label(self, text="STUDENT LOGIN", bg='#572a7f', fg='white', font=("Helvetica,", 24, 'bold'))
            self.label.place(x=475, y=90)
            self.label1 = Label(self, text="Student ID", bg='#351556', fg='white', font=("Helvetica", 18, 'bold'))
            self.label1.place(x=350, y=180)
            self.user_text = Entry(self, textvariable=self.a, width=45)
            self.user_text.place(x=480, y=190)
            self.label2 = Label(self, text="Password", bg='#1b0933', fg='white', font=("Helvetica", 18, 'bold'))
            self.label2.place(x=350, y=250)
            self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
            self.pass_text.place(x=480, y=255)
            self.butt = Button(self, text="Login", bg='white', font=10, width=8, command=chex).place(x=580, y=300)
            self.label3 = Label(self, text="COURSE MANAGEMENT SYSTEM", bg='#572a7f', fg='white',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=350, y=30)

        check()


Lib().mainloop()
