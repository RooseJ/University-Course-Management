from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Courses")
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.canvas = Canvas(width=1500, height=1500, bg='#572a7f')
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        l1 = Label(self, text="Student Search Catalog", bg='gold', font=("Arial", 20, 'bold')).place(x=475, y=20)
        l = Label(self, text="Search By:", bg='#572a7f', fg='white', font=("Helvetica", 15, 'bold')).place(x=350, y=96)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4],
                                                                     row[5], row[6], row[7]))

        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error.', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the ' + g.get())
            elif g.get() == 'Course Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select c.course_id, c.course_name, a.name, c.day, c.time, c.building, "
                                          "c.room, c.semester from course c, admin a where a.admin_id = c.admin_id "
                                          "and c.course_name LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Either the Course Name is Incorrect or is Not Available!")
                except Error:
                    messagebox.showerror("Error", "Something went wrong!")
            elif g.get() == 'Lecturer Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select c.course_id, c.course_name, a.name, c.day, c.time, c.building, "
                                          "c.room, c.semester from course c, admin a where a.admin_id = c.admin_id and "
                                          "a.admin_name LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Lecturer not Found!")
                except Error:
                    messagebox.showerror("Error.", "Something went wrong!")
            elif g.get() == 'Course ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select c.course_id, c.course_name, a.name, c.day, c.time, c.building, "
                                          "c.room, c.semester from course c, admin a where c.course_id a.admin_id = "
                                          "c.admin_id and LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Either Course ID is Incorrect or It Is Not Available")
                except Error:
                    messagebox.showerror("Error", "Something went wrong.")

        b = Button(self, text="Find", width=15, bg='gold', font=("Arial", 10, 'bold'), command=ge).place(x=800,
                                                                                                         y=148)
        c = ttk.Combobox(self, textvariable=g, values=["Course Name", "Lecturer Name", "Course ID"], width=40,
                         state="readonly").place(x=500, y=100)
        en = Entry(self, textvariable=f, width=43).place(x=500, y=155)
        la = Label(self, text="Enter:", bg='#572a7f', fg='white', font=("Helvetica", 15, 'bold')).place(x=350, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x, event.y) == "separator":
                return "break"

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
        ttk.Style().configure("Treeview", font=('Arial', 12))


Search().mainloop()
