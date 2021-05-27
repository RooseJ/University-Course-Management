from tkinter import *
from tkinter import messagebox
import os
import mysql.connector
from tkinter import ttk
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
        self.title("COURSE MANAGEMENT STUDENT")

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

        # creating table

        self.listTree = ttk.Treeview(self, height=14, columns=('Course', 'Lecturer', 'Days', 'Time', 'Building',
                                                               'Room Number', 'Semester'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='Course ID')
        self.listTree.column("#0", width=100, minwidth=100, anchor='center')
        self.listTree.heading("Course", text='Course Name')
        self.listTree.column("Course", width=200, minwidth=200, anchor='center')
        self.listTree.heading("Lecturer", text='Lecturer')
        self.listTree.column("Lecturer", width=200, minwidth=200, anchor='center')
        self.listTree.heading("Days", text='Days')
        self.listTree.column("Days", width=125, minwidth=125, anchor='center')
        self.listTree.heading("Time", text='Time')
        self.listTree.column("Time", width=125, minwidth=125, anchor='center')
        self.listTree.heading("Building", text='Building')
        self.listTree.column("Building", width=125, minwidth=125, anchor='center')
        self.listTree.heading("Room Number", text='Room Number')
        self.listTree.column("Room Number", width=125, minwidth=125, anchor='center')
        self.listTree.heading("Semester", text='Semester')
        self.listTree.column("Semester", width=125, minwidth=125, anchor='center')

        self.listTree.place(x=45, y=360)
        self.vsb.place(x=1165, y=361, height=287)
        self.hsb.place(x=45, y=650, width=1125)
        ttk.Style().configure("Treeview", font=('Arial', 10))

        # verifying input

        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD.")
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD.")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='course_management',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()
                    stud_id = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('Select * from `student` where stud_id= %s AND password = %s ',
                                   (stud_id, password,))
                    pc = cursor.fetchone()
                    if pc:
                        try:

                            self.conn = mysql.connector.connect(host='localhost',
                                                                database='course_management',
                                                                user='root',
                                                                password='')
                            cursor = conn.cursor()
                            cursor.execute(
                                "Select c.course_id, c.course_name, a.name, c.day, c.time, c.building, c.room, "
                                "c.semester  from issue_course ic, student s, course c, admin a "
                                "where ic.stud_id = s.stud_id and c.course_id = ic.course_id and a.admin_id = "
                                "c.admin_id and s.stud_id = %s",
                                [stud_id])
                            pc = cursor.fetchall()
                            if pc:
                                self.listTree.delete(*self.listTree.get_children())
                                for row in pc:
                                    self.listTree.insert("", 'end', text=row[0],
                                                         values=(row[1], row[2], row[3], row[4],
                                                                 row[5], row[6], row[7]))
                            else:
                                messagebox.showinfo("Error.", "Either th ID is Wrong or The Course Is Not Yet Issued.")

                        except Error:
                            messagebox.showerror("Error.", "Something Went Wrong!")
                    else:
                        print(pc)
                        messagebox.showinfo('Error.', 'Invalid username or password')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error.', "Something Went Wrong,Try Restarting.")

        def sea():
            os.system('%s %s' % (py, 'student_course.py'))

        def log():
            conf = messagebox.askyesno("Confirm", "Are you sure you want to Logout?")
            if conf:
                self.destroy()
                os.system('%s %s' % (py, 'Entry-point.py'))

        def check():

            self.label = Label(self, text="STUDENT PAGE", bg='#0D6CB7', fg='white', font=("Helvetica,", 24, 'bold'))
            self.label.place(x=475, y=90)
            self.label1 = Label(self, text="Student ID:", bg='#ffdf00', fg='black', font=("Helvetica", 18, 'bold'))
            self.label1.place(x=350, y=180)
            self.user_text = Entry(self, textvariable=self.a, width=45)
            self.user_text.place(x=490, y=190)
            self.label2 = Label(self, text="Password:", bg='#ffdf00', fg='black', font=("Helvetica", 18, 'bold'))
            self.label2.place(x=350, y=250)
            self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
            self.pass_text.place(x=490, y=255)
            self.butt = Button(self, text="Find Issued Courses", bg='#ffdf00', font=8, width=20, command=chex).place(
                x=340, y=300)
            self.butt = Button(self, text="Search Available Courses", bg='#ffdf00', font=8, width=25,
                               command=sea).place(
                x=625, y=300)
            self.label3 = Label(self, text="COURSE MANAGEMENT SYSTEM", bg='#0D6CB7', fg='white',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=350, y=30)
            self.brt = Button(self, text="LOGOUT", width=15, bg="red", font=('arial', 10),
                              command=log).place(x=1000, y=25)

        check()


Lib().mainloop()
