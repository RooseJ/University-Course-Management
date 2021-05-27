from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os,sys
py=sys.executable

#creating window
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('Add User')
        self.canvas = Canvas(width=500, height=417, bg="#441c55")
        self.canvas.pack()
#creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()


        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                         database='course_management',
                                         user='root',
                                         password='')
                self.myCursor = self.conn.cursor()
                self.myCursor.execute("Insert into admin(user,name,password) values (%s,%s,%s)",[u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Is Now in the System")
                ask = messagebox.askyesno("Confirm", "Do You Want to Add Another User?")
                if ask:
                    self.destroy()
                    os.system('%s %s' % (py, 'Add_User.py'))
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error!", "Something Went Wrong.")
#label and input
        Label(self, text='User Details:', bg='#FFDF00', fg='black', font=('Arial', 20, 'bold')).place(x=175, y=22)
        Label(self, text='Username:', bg='#441c55', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='Name:', bg='#441c55', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='Password:', bg='#441c55', fg='white', font=('Helvetica', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Submit", width=15, bg='#FFDF00',fg='black', font=('Arial', 10, 'bold'), command=insert).place(x=200, y=230)
reg().mainloop()