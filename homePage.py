# This is a sample Python script.
from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from tkintertable import TableCanvas, TableModel
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

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
        self.txt = ""
        self.count = 0
        self.text = ''
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", 30, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.slider()


        #self.profile = ImageTk.PhotoImage \
        #   (file='images\\profile.png')
        #self.profile_button = Button(self.window, command=profile, image=self.profile, relief=FLAT, borderwidth=0, cursor="hand2")
        #self.profile.place(x=0, y=0)

        self.courses = ImageTk.PhotoImage \
            (file='images\\courses.png')
        self.courses_button = Button(self.window, command=self.courses, image=self.courses, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.courses_button.place(x=0, y=200)

        self.timetable = ImageTk.PhotoImage \
            (file='images\\timetable.png')
        self.timetable_button = Button(self.window, command=self.timetable, image=self.timetable, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.timetable_button.place(x=0, y=600)

    def connectDB():
        pass
    
    def generateMessage():
        #generate latest messages
        pass 
    
    def sendEmails():
        #send emails
        pass

    def profile(self):
        pass

    def timetable(self):
        pass

    def courses(self):

        pass

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

def win():
    window = Tk()
    Id = 0
    HomePage(window, Id)
    window.mainloop()

win()