from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import mysql.connector
from mysql.connector import Error

py = sys.executable


# creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add Student')
        self.canvas = Canvas(width=500, height=417, bg='#9900cc')
        self.canvas.pack()
        n = StringVar()
        p = StringVar()
        a = StringVar()
        v = StringVar()

        # verifying input
        def asi():
            if len(n.get()) < 1:
                messagebox.showinfo("OOPS!", "Please Enter Student's Name.")
            elif len(p.get()) < 1:
                messagebox.showinfo("OOPS!", "Please Enter Student's Phone Number.")
            elif len(a.get()) < 1:
                messagebox.showinfo("OOPS!", "Please Enter Student's Address.")
            elif len(v.get()) < 1:
                messagebox.showinfo("OOPS!", "Please Enter Student's Password.")

            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    pw = v.get()
                    self.myCursor.execute("Insert into student(name,phone_number,address,password) values (%s,%s,%s,%s)",
                                          [name1, pn1, add1, pw])
                    self.conn.commit()
                    messagebox.showinfo("Done", "Student Has Been Added Successfully")
                    ask = messagebox.askyesno("Confirm", "Do You Want to Add Another Student?")
                    if ask:
                        self.destroy()
                        os.system('%s %s' % (py, 'Add_Student.py'))
                    else:
                        self.destroy()
                        self.myCursor.close()
                        self.conn.close()
                except Error:
                    messagebox.showerror("Error", "Something Went Wrong")

        # label and input box
        Label(self, text='Student Details', bg='#DB9200', fg='black', font=('Arial', 20, 'bold')).place(x=150, y=25)
        Label(self, text='Name:', bg='#9900cc', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=n, width=30).place(x=200, y=84)
        Label(self, text='Phone Number:', bg='#9900cc', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=p, width=30).place(x=200, y=132)
        Label(self, text='Address:', bg='#9900cc', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=a, width=30).place(x=200, y=182)
        Label(self, text='Password:', bg='#9900cc', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=230)
        Entry(self, textvariable=v, width=30).place(x=200, y=232)
        Button(self, text="Submit", width=15, bg='#DB9200', fg='black',
               font=('arial', 10, 'bold'), command=asi).place(x=230, y=280)


Add().mainloop()
