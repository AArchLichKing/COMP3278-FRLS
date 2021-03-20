# This is a sample Python script.
from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from tkintertable import TableCanvas, TableModel
import ctypes
import time
import mysql.connector


ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="facerecognition")
cursor = myconn.cursor()

class HomePage:
    def __init__(self, window, Id):
        self.window = window
        self.window.geometry("3200x2000+200+200")
        self.window.title("HKU Student System")
        self.window.resizable(False, False)
        self.database_frame = ImageTk.PhotoImage\
            (file='images\\home.png')
        self.image_panel = Label(self.window, image=self.database_frame)
        self.image_panel.pack(fill='both', expand='yes')
        self.txt = "home page"
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", 30, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.profile = ImageTk.PhotoImage \
            (file='images\\profile.png')
        self.profile_button = Button(self.window, command=self.profile, image=self.profile, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.profile_button.place(x=0, y=0)

        self.name = "Zhang Maoqi"
        self.clabel = Label(self.window, text= self.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=170, y=380)

        self.clabel = Label(self.window, text="Current time", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=100, y=480)
        self.label = Label(self.window, text="", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.update_clock()
        self.label.place(x=450, y=480)
        """self.lastlogin = Label(self.window, text="Last login", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.lastlogin.place(x=100, y=500)"""

        self.courses = ImageTk.PhotoImage \
            (file='images\\courses.png')
        self.courses_button = Button(self.window, command=self.courses, image=self.courses, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.courses_button.place(x=0, y=800)

        self.timetable = ImageTk.PhotoImage \
            (file='images\\timetable.png')
        self.timetable_button = Button(self.window, command=self.timetable, image=self.timetable, relief=FLAT, borderwidth=0,
                                     cursor="hand2")

        self.timetable_button.place(x=0, y=600)

        self.deadline = ImageTk.PhotoImage \
            (file='images\\deadline.png')
        self.deadline_button = Button(self.window, command=self.timetable, image=self.deadline, relief=FLAT,
                                       borderwidth=0,
                                       cursor="hand2")

        self.deadline_button.place(x=0, y=1000)

    def connectDB():
        pass
    
    def generateMessage():
        #generate latest messages
        pass 
    
    def sendEmails():
        #send emails
        if (False):
            success("send emails")

    def profile(self):
        pass

    def timetable(self):
        pass

    def courses(self):
        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(self.window, yscrollcommand=scrollbar.set)
        for line in range(100):
            mylist.insert(END, "This is line number " + str(line))
        mylist.pack(side=LEFT, fill=BOTH)
        self.courses = ImageTk.PhotoImage \
            (file='images\\courses.png')
        self.courses_button = Button(self.window, command=self.courses, image=self.courses, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.courses_button.place(x=400, y=800)

    def generateClassTable():
        #generate class table
        tframe = Frame(master)
        tframe.pack()
        table = TableCanvas(tframe)
        table.show()

    def slider(self):
        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)
        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1
        self.heading.after(100, self.slider)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.window.after(1000, self.update_clock)


# a success window that shows "Successfully " + task each time when something completed by system
class success:
    def __init__(self, task, filepath):
        self.txt = "Successfully " + task
        self.window = Tk()
        self.window.geometry("800x500+800+800")
        self.window.title("success!")
        self.window.resizable(False, False)
        image = Image.open(filepath)
        image = image.resize((800, 500), Image.ANTIALIAS)
        self.database_frame = ImageTk.PhotoImage(image)
        self.image_panel = Label(self.window, image=self.database_frame)
        self.image_panel.pack(fill='both', expand='yes')
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.msg.place(x=20, y=200)
        self.window.mainloop()

def win():
    window = Tk()
    Id = 0
    HomePage(window, Id)
    window.mainloop()

#test function for success windows
def testSuc(filepath):
    success("send to your emails!", filepath)

win()
#file = "images\\Success\\email.png"
#testSuc(file)