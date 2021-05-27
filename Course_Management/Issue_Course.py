from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys

py = sys.executable


# creating window
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title('Administration')
        self.maxsize(440, 300)
        self.canvas = Canvas(width=1366, height=768, bg='#1b0933')
        self.canvas.pack()
        c = StringVar()
        d = StringVar()

        # verifying input
        def isb():
            if (len(c.get())) == 0:
                messagebox.showinfo('Error.', 'Empty field!')
            elif (len(d.get())) == 0:
                messagebox.showinfo('Error.', 'Empty field!')
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    try:
                        print("success")
                        course = c.get()
                        student = d.get()
                        self.mycursor.execute(
                            "Insert into issue_course(course_id, stud_id) values (%s,%s)",
                            [course, student])
                        self.conn.commit()
                        messagebox.showinfo("Success", "Course Has Been Issued!")
                        ask = messagebox.askyesno("Confirm", "Do you want to add another?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'Issue_Course.py'))
                        else:
                            self.destroy()
                    except Error:
                        messagebox.showerror("Error.", "Check The Details!")
                except Error:
                    messagebox.showerror("Error.", "Something Went Wrong!")

        # label and input box
        Label(self, text='Course Issuing', bg='#ffdf00', font=('Arial', 20, 'bold')).place(x=135, y=40)
        Label(self, text='Course ID:', bg='#1b0933', font=('Helvetica', 10, 'bold'), fg='white').place(x=30, y=100)
        Entry(self, textvariable=c, width=40).place(x=160, y=106)
        Label(self, text='Student ID:', bg='#1b0933', font=('Helvetica', 10, 'bold'), fg='white').place(x=20, y=150)
        Entry(self, textvariable=d, width=40).place(x=160, y=158)
        Button(self, text="Issue", bg='gold', font=('arial', 10, 'bold'), width=20, command=isb).place(x=200, y=200)


issue().mainloop()
