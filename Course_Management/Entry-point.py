from tkinter import *

import os
import sys

py = sys.executable


# creating window
class entry(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title('Welcome')
        self.maxsize(600, 300)
        self.canvas = Canvas(width=1366, height=768, bg='#1b0933')
        self.canvas.pack()

        def admin():
            self.destroy()
            os.system('%s %s' % (py, 'Log_in.py'))

        def stud():
            self.destroy()
            os.system('%s %s' % (py, 'student_main.py'))

        # label and input box
        Label(self, text='Please Choose Level of Access', bg='#ffdf00', font=('Arial', 20, 'bold')).place(x=80, y=50)
        Button(self, text="Admin", bg='gold', font=('arial', 10, 'bold'), width=20, command=admin).place(x=200, y=150)
        Button(self, text="Student", bg='gold', font=('arial', 10, 'bold'), width=20, command=stud).place(x=200, y=225)


entry().mainloop()
