from tkinter import *
from tkinter import messagebox
import os
import sys
from PIL import ImageTk, Image

import mysql.connector
from mysql.connector import Error

py = sys.executable


# creating window
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(1320, 768)
        self.minsize(1320, 768)
        self.title('MAIN MENU')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

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

        # calling scripts
        def a_s():
            os.system('%s %s' % (py, 'Add_Student.py'))

        def a_b():
            os.system('%s %s' % (py, 'Add_Courses.py'))

        def r_c():
            os.system('%s %s' % (py, 'remove_course.py'))

        def r_s():
            os.system('%s %s' % (py, 'Remove_student.py'))

        def ic():
            os.system('%s %s' % (py, 'Issue_Course.py'))

        def ret():
            os.system('%s %s' % (py, 'Remove_Course.py'))

        def sea():
            os.system('%s %s' % (py, 'Courses.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'Log_In.py'))

        # def handle(event):
        def add_user():
            os.system('%s %s' % (py, 'Add_User.py'))

        def rem_user():
            os.system('%s %s' % (py, 'Remove_User.py'))

        def sest():
            os.system('%s %s' % (py, 'Student.py'))

        def ser():
            if len(self.studid.get()) == 0:
                messagebox.showinfo("Error", "Empty Field!")
            else:

                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='course_management',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()
                    change = int(self.studid.get())
                    cursor.execute(
                        "Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_course bi,"
                        "student s,course b where s.stud_id = bi.stud_id and b.course_id = bi.course_id and "
                        "s.stud_id = %s",
                        [change])
                    pc = cursor.fetchall()
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
                    else:
                        messagebox.showinfo("Error.", "ID is Wrong or The Course is Not Yet Issued on This ID")
                except Error:
                    # print(Error)
                    messagebox.showerror("Error.", "Something Went Wrong!")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',
                                               database='course_management',
                                               user='root',
                                               password='')
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error.", "Please Register A User!")
                    x = messagebox.askyesno("Confirm", "Do You Want to Register a User?")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_User.py'))
                else:
                    # label and input box
                    self.label3 = Label(self, text='COURSE MANAGEMENT SYSTEM', fg='white', bg="#0D6CB7",
                                        font=('Helvetica', 30, 'bold'))
                    self.label3.place(x=350, y=22)
                    self.label4 = Label(self, text='ADMIN PAGE', fg='white', bg="#0D6CB7",
                                        font=('Helvetica', 20, 'bold'))
                    self.label4.place(x=570, y=85)

                    self.button = Button(self, text='Add Student', width=25, bg="gold", font=('arial', 10),
                                         command=a_s).place(x=240, y=215)
                    self.button = Button(self, text='Add Course', width=25, bg="gold", font=('arial', 10),
                                         command=a_b).place(x=610, y=215)
                    self.brt = Button(self, text="Add User", width=15, bg="gold", font=('arial', 10),
                                      command=add_user).place(x=1000, y=215)
                    self.button = Button(self, text='Search Student', width=25, bg="gold", font=('arial', 10),
                                         command=sest).place(x=240, y=500)
                    self.button = Button(self, text='Search Course', width=25, bg="gold", font=('arial', 10),
                                         command=sea).place(x=610, y=500)
                    self.brt = Button(self, text="Issue Course", width=15, bg="gold", font=('arial', 10),
                                      command=ic).place(x=1000, y=500)

                    self.brt = Button(self, text="LOGOUT", width=15, bg="red", font=('arial', 10),
                                      command=log).place(x=1150, y=25)
            except Error:
                messagebox.showerror("Error.", "Something Went Wrong!")

        check()


MainWin().mainloop()
