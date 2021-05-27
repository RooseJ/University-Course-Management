from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys

py = sys.executable


# creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 600)
        self.minsize(500, 600)
        self.title('Add Course')
        self.canvas = Canvas(width=600, height=600, bg='#572a7f')
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()
        g = StringVar()

        # verifying Input
        def b_q():
            if len(a.get()) == 0 or len(b.get()) == 0 or len(c.get()) == 0 or len(d.get()) == 0 or len(e.get()) == 0 \
                    or len(f.get()) == 0 or len(g.get()) == 0:
                messagebox.showerror("Error.", "Please Enter The Details!")
            else:

                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute(
                        "Insert into course(course_name,admin_id,day,time,building,room,semester) values (%s,%s,%s,"
                        "%s,%s,%s,%s)",
                        [a.get(), b.get(), c.get(), d.get(), e.get(), f.get(), g.get()])
                    self.conn.commit()
                    messagebox.showinfo('Success', "Course Has Been Added!")
                    ask = messagebox.askyesno("Confirmed.", "Do You Want to Add Another Course?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Courses.py'))
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error.", "Please Check The Details!")

        # creating input box and label
        Label(self, text='').pack()
        Label(self, text='Course Details:', bg='gold', fg='black', font=('Arial', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='Course Name:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=180)
        Entry(self, textvariable=a, width=30).place(x=190, y=182)
        Label(self, text='Lecturer Admin ID:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=230)
        Entry(self, textvariable=b, width=30).place(x=190, y=232)
        Label(self, text='Days:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=280)
        Entry(self, textvariable=c, width=30).place(x=190, y=282)
        Label(self, text='Time:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=330)
        Entry(self, textvariable=d, width=30).place(x=190, y=332)
        Label(self, text='Building Name:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=380)
        Entry(self, textvariable=e, width=30).place(x=190, y=382)
        Label(self, text='Room Number:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=430)
        Entry(self, textvariable=f, width=30).place(x=190, y=432)
        Label(self, text='Semester:', bg='#572a7f', fg='white', font=('Helvetica', 10, 'bold')).place(x=40, y=480)
        Entry(self, textvariable=g, width=30).place(x=190, y=482)
        Button(self, text="Submit", bg= 'gold', font=('arial', 10, 'bold'), command=b_q).place(x=245, y=540)


Add().mainloop()
