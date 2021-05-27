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
        self.maxsize(800, 500)
        self.minsize(800, 500)
        self.canvas = Canvas(width=800, height=500, bg='#572a7f')
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        l1 = Label(self, text="Search Catalog", bg='gold', font=("Arial", 20, 'bold')).place(x=290, y=20)
        l = Label(self, text="Search By", bg='#572a7f', fg='white', font=("Helvetica", 15, 'bold')).place(x=60, y=96)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))

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
                    self.mycursor.execute("Select * from course where course_name LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Either the Course Name is Incorrect or is Not Available!")
                except Error:
                    messagebox.showerror("Error", "Something went wrong!")
            elif g.get() == 'Lecturer ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from course where admin_id LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Lecturer Admin ID not Found!")
                except Error:
                    messagebox.showerror("Error.", "Something went wrong!")
            elif g.get() == 'Course ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='course_management',
                                                        user='root',
                                                        password='')
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from course where course_id LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Try Again.", "Either Course ID is Incorrect or It Is Not Available")
                except Error:
                    messagebox.showerror("Error", "Something went wrong.")

        b = Button(self, text="Find", width=15, bg='gold', font=("Arial", 10, 'bold'), command=ge).place(x=460,
                                                                                                         y=148)
        c = ttk.Combobox(self, textvariable=g, values=["Course Name", "Lecturer ID", "Course ID"], width=40,
                         state="readonly").place(x=180, y=100)
        en = Entry(self, textvariable=f, width=43).place(x=180, y=155)
        la = Label(self, text="Enter", bg='#572a7f', fg='white', font=("Helvetica", 15, 'bold')).place(x=100, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        self.listTree = ttk.Treeview(self, height=13, columns=('Course Name', 'Lecturer ID', 'Availability'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Course ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Course Name", text='Course Name')
        self.listTree.column("Course Name", width=200, anchor='center')
        self.listTree.heading("Lecturer ID", text='Lecturer Admin ID')
        self.listTree.column("Lecturer ID", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=763, y=200, height=287)
        ttk.Style().configure("Treeview", font=('Helvetica', 10))


Search().mainloop()
