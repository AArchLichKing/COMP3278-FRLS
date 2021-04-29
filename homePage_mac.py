# This is a sample Python script.
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import time
from object import Student, Course
import mysql.connector
from functools import partial
import re
import datetime
import webbrowser

import smtplib
from email.mime.text import MIMEText
## import packages for send_email()
import pandas as pd

## import packages for generateClassTable()

# ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Tyd3035534775", database="createDB")
cursor = myconn.cursor()

size = 0.4


def time_convert(time):
    seconds = time.seconds
    hour = str(seconds // 3600)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str((seconds // 60) % 60)
    if len(minute) == 1:
        minute = "0" + minute
    return hour + ":" + minute

class HomePage:
    def __init__(self, window, Id):
        global size
        self.i=size
        self.Id = Id
        self.current_panel = 2
        self.window = window
        change = str(int(3200*self.i))+'x'+str(int(2000*self.i))+'+' + str(int(200*self.i)) + '+' + str(int(100*self.i))
        self.window.geometry(change)
        self.window.title("HKU Student System")
        self.window.resizable(False, False)

        self.student = Student(Id)
        self.courses = Course(Id)
        style = ttk.Style(window)
        style.configure('lefttab.TNotebook', tabposition='wn')

        notebook = ttk.Notebook(window, style='lefttab.TNotebook')
        img = Image.open("images/subframe.png")
        img = img.resize((int(2480*self.i), int(2001*self.i)), Image.ANTIALIAS)
        self.subframe = ImageTk.PhotoImage(img)

        self.f1 = Frame(notebook, bg="white")
        self.f2 = Frame(notebook, width=int(1000*self.i), height=int(1000*self.i))
        self.f3 = Frame(notebook, width=int(1000*self.i), height=int(1000*self.i))
        self.f4 = Frame(notebook, width=int(1000*self.i), height=int(1000*self.i))

        img = Image.open("images/Profile.png")
        img = img.resize((int(722*self.i), int(602*self.i)), Image.ANTIALIAS)
        self.profile = ImageTk.PhotoImage(img)
        img = Image.open("images/courses.png")
        img = img.resize((int(722*self.i), int(202*self.i)), Image.ANTIALIAS)
        self.coursestab = ImageTk.PhotoImage(img)
        img = Image.open("images/timetable.png")
        img = img.resize((int(722*self.i), int(202*self.i)), Image.ANTIALIAS)
        self.timetable = ImageTk.PhotoImage(img)
        img = Image.open("images/deadline.png")
        img = img.resize((int(722*self.i), int(202*self.i)), Image.ANTIALIAS)
        self.deadline = ImageTk.PhotoImage(img)
        
        notebook.add(self.f1, text='Frame 1', image=self.profile)
        notebook.add(self.f2, text='Frame 2', image=self.timetable)
        notebook.add(self.f3, text='Frame 3', image=self.coursestab)
        notebook.add(self.f4, text='Frame 4', image=self.deadline)
        img = Image.open("images/f1.png")
        img = img.resize((int(2480*self.i), int(2000*self.i)), Image.ANTIALIAS)
        self.subframe1 = ImageTk.PhotoImage(img)
        img = Image.open("images/f2.png")
        img = img.resize((int(2480*self.i), int(2000*self.i)), Image.ANTIALIAS)
        self.subframe2 = ImageTk.PhotoImage(img)
        img = Image.open("images/f3.png")
        img = img.resize((int(2480*self.i), int(2000*self.i)), Image.ANTIALIAS)
        self.subframe3 = ImageTk.PhotoImage(img)
        img = Image.open("images/f4.png")
        img = img.resize((int(2480*self.i), int(2000*self.i)), Image.ANTIALIAS)
        self.subframe4 = ImageTk.PhotoImage(img)
        self.image_panel = Label(self.f1, image=self.subframe1)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f2, image=self.subframe2)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f3, image=self.subframe3)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f4, image=self.subframe4)
        self.image_panel.pack(fill='both', expand='yes')
        img = Image.open("images/ttFrame.png")
        img = img.resize((int(1820*self.i), int(1200*self.i)), Image.ANTIALIAS)
        self.ttF = ImageTk.PhotoImage(img)
        self.image_panel = Label(self.f2, image=self.ttF)
        self.image_panel.place(x=int(300*self.i), y=int(700*self.i))
        img = Image.open("images/coursegrid.png")
        img = img.resize((int(1200*self.i), int(400*self.i)), Image.ANTIALIAS)
        self.coursegrid = ImageTk.PhotoImage(img)

        notebook.grid(row=0, column=0, sticky="nw")
        self.txt = "home page"
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", 30, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)

        self.name = self.student.name
        self.clabel = Label(self.window, text=self.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=int(170*self.i), y=int(380*self.i))

        self.clabel = Label(self.window, text="Current time", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=int(100*self.i), y=int(480*self.i))
        self.label = Label(self.window, text="", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.update_clock()
        self.label.place(x=int(450*self.i), y=int(480*self.i))
        self.timetable2 = generateClassTable(self.student, self.courses)
        img = Image.open("images/timegrid.png")
        img = img.resize((int(300*self.i), int(60*self.i)), Image.ANTIALIAS)
        self.timegrid = ImageTk.PhotoImage(img)
        img = Image.open("images/tutorialgrid.png")
        img = img.resize((int(300*self.i), int(60*self.i)), Image.ANTIALIAS)
        self.tutorialgrid = ImageTk.PhotoImage(img)
        self.X = len(self.timetable2)
        self.Y = len(self.timetable2.columns)  # 5
        self.l_name = Label(self.f1, text=self.student.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.l_name.place(x=int(400*self.i), y=int(285*self.i))
        self.l_email = Label(self.f1, text=self.student.email_addr, bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", 13, "bold"))
        self.l_email.place(x=int(500*self.i), y=int(585*self.i))
        self.l_user_id = Label(self.f1, text=self.student.username, bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.l_user_id.place(x=int(500*self.i), y=int(385*self.i))
        self.l_year = Label(self.f1, text=self.student.admitted_year, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.l_year.place(x=int(600*self.i), y=int(485*self.i))
        self.login = Label(self.f1, text=self.student.login_time, bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.login.place(x=int(600*self.i), y=int(1685*self.i))
        self.logout = Label(self.f1, text=self.student.logout_time, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.logout.place(x=int(600*self.i), y=int(1585*self.i))
        self.duration = Label(self.f1, text=self.student.duration, bg="white", fg="#4f4e4d",
                              font=("yu gothic ui", 13, "bold"))
        self.duration.place(x=int(600*self.i), y=int(1785*self.i))
        img = Image.open("images/changeemail.png")
        img = img.resize((int(657*self.i), int(135*self.i)), Image.ANTIALIAS)
        self.changee = ImageTk.PhotoImage(img)
        self.changee_button = Button(self.f1, command=partial(self.change, "email", self.student), image=self.changee,
                                     relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.changee_button.place(x=int(100*self.i), y=int(740*self.i))
        img = Image.open("images/changepw.png")
        img = img.resize((int(657*self.i), int(135*self.i)), Image.ANTIALIAS)
        self.changepw = ImageTk.PhotoImage(img)
        self.changepw_button = Button(self.f1, image=self.changepw, command=partial(self.change, "password", self.student),
                                      relief=FLAT, borderwidth=0,
                                      cursor="hand2")
        self.changepw_button.place(x=int(850*self.i), y=int(740*self.i))
        self.notice = Label(self.f4, text="Deadline notification", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.notice.place(x=int(100*self.i), y=int(400*self.i))
        self.CheckCourse(self.courses)
        k = len(self.courses.course_name)
        self.subnotebook = ttk.Notebook(self.f3)
        self.Lecture = Frame(self.subnotebook, width=int(3000*self.i), height=int(2000*self.i))
        self.Tutorial = Frame(self.subnotebook, bg="white", width=int(3000*self.i), height=int(2000*self.i))
        self.subnotebook.add(self.Lecture, text='Lecture')
        self.subnotebook.add(self.Tutorial, text='Tutorial')
        self.subnotebook.place(x = 0, y = int(200*self.i))
        self.filterTutorial()
        self.course_panel = []
        self.tutorial_panel = []
        self.tgrid = []
        self.lgrid = []
        for i in range(len(self.L)):
            m = i // 2
            n = i % 2
            img = Image.open("images/coursegrid.png")
            img = img.resize((int(1200*self.i), int(400*self.i)), Image.ANTIALIAS)
            self.lgrid.append(ImageTk.PhotoImage(img))
            self.course_panel.append(Button(self.Lecture, image=self.lgrid[i], command = partial(self.Coursewindow, self.L[i])))
            self.course_panel[i].place(x=int(80*self.i) + n * int(1200*self.i), y=int(100*self.i) + m * int(500*self.i))
            self.course_info1 = Label(self.Lecture, text=self.courses.course_name[self.L[i]])
            self.course_info1.place(x=int(90*self.i) + n * int(1200*self.i), y=int(110*self.i) + m * int(500*self.i))
            self.course_info2 = Label(self.Lecture, text=self.courses.course_long_name[self.L[i]])
            self.course_info2.place(x=int(90*self.i) + n * int(1200*self.i), y=int(170*self.i) + m * int(500*self.i))
            self.course_info3 = Label(self.Lecture, text="Instructor: "+ self.courses.instructor[self.L[i]])
            self.course_info3.place(x=int(90*self.i) + n * int(1200*self.i), y=int(230*self.i) + m * int(500*self.i))
        for i in range(len(self.T)):
            m = i // 2
            n = i % 2
            img = Image.open("images/coursegrid.png")
            img = img.resize((int(1200*self.i), int(400*self.i)), Image.ANTIALIAS)
            self.tgrid.append(ImageTk.PhotoImage(img))
            self.tutorial_panel.append(Button(self.Tutorial, image=self.tgrid[i], command = partial(self.Coursewindow, self.T[i])))
            self.tutorial_panel[i].place(x=int(80*self.i) + n * int(1200*self.i), y=int(100*self.i) + m * int(500*self.i))
            self.course_info1 = Label(self.Tutorial, text=self.courses.course_name[self.T[i]])
            self.course_info1.place(x=int(90*self.i) + n * int(1200*self.i), y=int(110*self.i) + m * int(500*self.i))
            self.course_info2 = Label(self.Tutorial, text=self.courses.course_long_name[self.T[i]])
            self.course_info2.place(x=int(90*self.i) + n * int(1200*self.i), y=int(170*self.i) + m * int(500*self.i))
            self.course_info3 = Label(self.Tutorial, text="Instructor: " + self.courses.instructor[self.T[i]])
            self.course_info3.place(x=int(90*self.i) + n * int(1200*self.i), y=int(230*self.i) + m * int(500*self.i))

        self.update_clock()
        notebook.select(self.f2)

        for i in range(self.X):
            for j in range(self.Y):
                if (isinstance(self.timetable2.iloc[i, j], str)):
                    if  re.search("Tutorial", self.timetable2.iloc[i, j]):
                        self.tt = Label(self.f2, image=self.tutorialgrid, relief=FLAT, borderwidth=0,  cursor="hand2")
                        self.ttlabel = Label(self.f2, text=self.timetable2.iloc[i, j], font=("yu gothic ui", 6, "bold"),
                                         bg="pale green")
                    else:
                        self.tt = Label(self.f2, image=self.timegrid, relief=FLAT, borderwidth=0,  cursor="hand2")
                        self.ttlabel = Label(self.f2, text=self.timetable2.iloc[i, j], font=("yu gothic ui", 6, "bold"),
                                         bg="pale turquoise")
                    a = int(600*self.i) + int(300*self.i) * j        
                    b = int(800*self.i) + int(60*self.i) * (i - 1)
                    self.tt.place(x=a, y=b)
                    self.ttlabel.place(x=a, y=b)

    def Coursewindow(self, num):
        self.window2 = Toplevel(self.window)
        self.window2.geometry("")
        self.window2.title(self.courses.course_name[num]+"  "+ self.courses.course_long_name[num])
        self.window2.resizable()
        img = Image.open("images/subcourse.png")
        img = img.resize((int(1809*self.i), int(2016*self.i)), Image.ANTIALIAS)
        self.f = ImageTk.PhotoImage(img)
        self.fw = Label(self.window2, image=self.f)
        self.fw.pack(fill='both', expand='yes')
        self.msg = Label(self.window2, text=self.courses.course_name[num]+"  "+ self.courses.course_long_name[num],
                         font=("yu gothic ui", 10, "bold"))
        self.msg.place(x=int(120*self.i), y=int(250*self.i))
        self.start_time = Label(self.window2, text="Instructor: " + self.courses.instructor[num], font=("yu gothic ui", 10, "bold"), bg = "white")
        self.start_time.place(x=int(120*self.i), y=int(400*self.i))
        self.duration_time = Label(self.window2, text="Office: "+self.courses.office[num], font=("yu gothic ui", 10, "bold"), bg = "white")
        self.duration_time.place(x=int(120*self.i), y=int(500*self.i))
        self.offHour = Label(self.window2, text= "Office Hour: " + self.courses.office_hour[num], font=("yu gothic ui", 10, "bold"), bg = "white")
        self.offHour.place(x=int(120*self.i), y=int(600*self.i))
        self.zoomlinkl = Label(self.window2, text="Zoom Link:",
                              font=("yu gothic ui", 10, "bold"), bg="white")
        self.zoomlinkl.place(x=int(120*self.i), y=int(800*self.i))
        self.zoomlink = Message(self.window2, text=self.courses.zoom_link[num],
                             font=("yu gothic ui", 10, "bold"), bg="white", width = int(1200*self.i))
        self.zoomlink.place(x=int(110*self.i), y=int(900*self.i))
        self.zoomlink.bind("<Button-1>", callback)
        self.w2 = Frame(self.window2, bg = "RED", width = int(2000*self.i), height = int(800*self.i))
        self.w2.place(x = 0, y = int(2000*self.i))
        sb = Scrollbar(self.w2)
        sb.pack(side=RIGHT, fill=Y)
        mylist = Listbox(self.w2, yscrollcommand=sb.set, width = int(83*self.i))
        for line in range(30):
            mylist.insert(END, "Number 000000000000" + str(line))
        mylist.pack(side=LEFT)
        sb.config(command=mylist.yview)

        self.zoomlinkl = Label(self.window2, text="Site: "+ self.courses.building_name[num]+self.courses.room_number[num],
                               font=("yu gothic ui", 10, "bold"), bg="white")
        self.zoomlinkl.place(x=int(120*self.i), y=int(700*self.i))
        self.mn = Label(self.window2, text=self.courses.material_name[num],
                              font=("yu gothic ui", 10, "bold"), bg="white")
        self.mn.place(x=int(120*self.i), y=int(1200*self.i))
        self.md = Label(self.window2, text=self.courses.material_date[num],
                          font=("yu gothic ui", 10, "bold"), bg="white")
        self.md.place(x=int(120*self.i), y=int(1300*self.i))
        self.ml = Label(self.window2, text=self.courses.material_link[num],
                          font=("yu gothic ui", 10, "bold"), bg="white")
        self.ml.place(x=int(120*self.i), y=int(1400*self.i))
        self.ml.bind("<Button-1>", callback)

        img = Image.open("images/20-20.png")
        img = img.resize((int(860*self.i), int(109*self.i)), Image.ANTIALIAS)
        self.email = ImageTk.PhotoImage(img)
        self.email_b = Button(self.window2, image=self.email,
                              command=partial(self.sendEmails, self.student, self.courses, num, ""))
        self.email_b.place(x=int(20*self.i), y=int(1900*self.i))

    def filterTutorial(self):
        k = len(self.courses.course_type)
        self.T = []
        self.L = []
        for i in range(k):
            if self.courses.course_type[i] =="Tutorial":
                self.T.append(i)
            else:
                self.L.append(i)

    def change(self, task, student):
        ChangeWin(self.window, task, student)
        self.student = Student(self.Id)

    def sendEmails(self, s, c, num, begin = "The following course will begin within an hour."):
        # send emails
        ## set up sender's account
        address = "maoqi@connect.hku.hk" #s.email_addr
        content = """Dear {0} ({1}):

        {18} The corresponding course materials are attached below for your reference.

        Course code: {2}
        Course name: {17}
        Course type: {3}
        Time: {4} {5}-{6}
        Building: {7}
        Room: {8}
        Zoom link: {9}
        Material name: {10}
        Released date: {11}
        Material link: {12}
        Instructor: {13}
        Office: {14}
        Office hour: {15}
        Teacher's message: {16}

    Please check the course information and rememeber to take your course on time.

    Best regards,
    eLearning Team
        """.format(s.name, s.email_addr, c.course_name[num], c.course_type[num], c.weekday[num],
                   time_convert(c.start_time[num]), time_convert(c.start_time[num] + c.duration[num]),
                   c.building_name[num], c.room_number[num], c.zoom_link[num], c.material_name[num],
                   c.material_date[num], c.material_link[num], c.instructor[num], c.office[num], c.office_hour[num],
                   c.message[num], c.course_long_name[num], begin)

        mail_host = 'smtp.163.com'
        mail_user = 'comp3278_group2'
        mail_pass = 'UGQEGXIPKFFLNHEQ'
        sender = 'comp3278_group2@163.com'
        receiver = [address]

        ## set up email information
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = 'HKU Course Notices'
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receiver)

        ## send email
        smtp0bj = smtplib.SMTP_SSL(mail_host, 465)
        smtp0bj.login(mail_user, mail_pass)
        smtp0bj.sendmail(sender, receiver, message.as_string())
        smtp0bj.quit()
        success("send the emails!", self.window)

    def CheckCourse(self, course):
        now = time.strftime("%H:%M:%S")
        current = TimeConverter(now)
        today = datetime.datetime.today().weekday()
        flag = False
        num = 0
        for i in range(len(course.start_time)):
            start = course.start_time[i]
            weekday = course.weekday[i]
            duration = course.duration[i]
            D = ["MON", "TUE", "WED", "THU", "FRI"]
            d = dict(enumerate(D))
            if (weekday == d.get(today)):
                if (start.seconds - current <= 3600) and (start.seconds >= current):
                    flag = True
                    num = i
                    break
                elif (start.seconds+duration.seconds  >= current and start.seconds < current):
                    num = -i
                    flag = True
                    break
        if flag == True and num >= 0:
             upcoming = "You have class {} in ten minutes!\n Click the right button to send details to your email".format(course.course_name[num])
             self.msg(upcoming, 1, num)
        elif flag:
             current = "You are currently taking {}! \n Click the right button to send details to your email".format(course.course_name[-num])
             self.msg(current, 1, -num)
        else:
             self.msg("No courses in ten minutes, check timetable for details", 0,0)

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

    def msg(self, text, y, num):
        if y == 1:

            img = Image.open("images/haveclass.png")
            img = img.resize((int(1802*self.i), int(252*self.i)), Image.ANTIALIAS)
            self.haveclassbg = ImageTk.PhotoImage(img)
            self.haveclass = Label(self.f2, image=self.haveclassbg,
                                       relief=FLAT, borderwidth=0,
                                       cursor="hand2")
            self.haveclass.place(x=int(300*self.i), y=int(350*self.i))
            img = Image.open("images/checkButton.png")
            img = img.resize((int(147*self.i), int(148*self.i)), Image.ANTIALIAS)
            self.checkButton = ImageTk.PhotoImage(img)
            self.check_button = Button(self.f2, image=self.checkButton, command=partial(self.sendEmails, self.student, self.courses, num),
                                       relief=FLAT, borderwidth=0,                                                                                 
                                       cursor="hand2")                                                                                             
            self.check_button.place(x=int(1900*self.i), y=int(400*self.i))
        else:
            img = Image.open("images/Noclass.png")
            img = img.resize((int(1802*self.i), int(252*self.i)), Image.ANTIALIAS)
            self.noclassbg = ImageTk.PhotoImage(img)
            self.noclass = Label(self.f2, image=self.noclassbg, 
                relief=FLAT, borderwidth=0, cursor="hand2")
            self.noclass.place(x=int(300*self.i), y=int(350*self.i))
        self.msg = Label(self.f2, text = text, font=("yu gothic ui", 13, "bold"))
        self.msg.place(x=int(400*self.i), y=int(400*self.i))

    def display_course(self, window, courses, num, i):
        m = i//2
        n = i % 2
        img = Image.open("images/coursegrid.png")
        img = img.resize((int(1200*self.i), int(400*self.i)), Image.ANTIALIAS)
        self.coursegrid = ImageTk.PhotoImage(img)
        self.image_panel = Button(window, image=self.coursegrid, command=partial(self.Coursewindow, courses, num))
        self.image_panel.place(x=int(80*self.i)+n*int(1200*self.i), y=int(400*self.i)+m*int(500*self.i))
        self.course_info = Label(window, text = courses.course_name[num] )
        self.course_info.place(x=int(90*self.i) + n * int(1200*self.i), y=int(410*self.i) + m * int(500*self.i))
        self.course_info = Label(window, text=courses.instructor[num])
        self.course_info.place(x=int(90*self.i) + n * int(1200*self.i), y=int(470*self.i) + m * int(500*self.i))

class successWin:
    def __init__(self, task, window):
        global size
        self.i=size
        self.txt = "Successfully " + task
        self.window = Toplevel(window)
        self.window.geometry("800x500+800+800")
        self.window.title("success!")
        self.successbg =ImageTk.PhotoImage \
                      (file='images/successbg.png')
        self.bg = Button(self.window, image=self.successbg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 10, "bold"))
        self.msg.place(x=int(80*self.i), y=int(200*self.i))
        self.window.mainloop()

def success(task,window):
    S = successWin(task, window)
    S.window.mainloop()

class FailureWin:
    def __init__(self, task, window):
        global size
        self.i=size
        self.txt = "Problems: unable to " + task+", \nyou need to check your input."
        self.window = Toplevel(window)
        change = str(int(800*self.i))+'x'+str(int(500*self.i))+'+'+str(int(800*self.i))+'+'+str(int(800*self.i))
        self.window.geometry(change)
        self.window.title("Warning!")
        img = Image.open("images/failurebg.png")
        img = img.resize((int(800*self.i), int(500*self.i)), Image.ANTIALIAS)
        self.failurebg =ImageTk.PhotoImage(img)
        self.bg = Button(self.window, image=self.failurebg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 10, "bold"))
        self.msg.place(x=int(80*self.i), y=int(200*self.i))
        self.window.mainloop()

def failure(task,window):
    S = FailureWin(task,window)
    S.window.mainloop()

def generateClassTable(student, course):
    # generate class table
    # class_name, start_time and end_time are lists containing each course's information
    class_name = course.course_name
    start_time = [time_convert(i) for i in course.start_time]
    end_time = [time_convert(course.start_time[i] + course.duration[i]) for i in range(len(course.start_time))]
    day = course.weekday
    time_list = ["09:00-09:30", "09:30-10:00", "10:00-10:30", "10:30-11:00", "11:00-11:30", "11:30-12:00",
                 "12:00-12:30", "12:30-13:00", "13:00-13:30", "13:30-14:00", "14:00-14:30", "14:30-15:00",
                 "15:00-15:30", "15:30-16:00", "16:00-16:30", "16:30-17:00", "17:00-17:30", "17:30-18:00",
                 "18:00-18:30"]

    week_list = ['MON', 'TUE', 'WED', 'THU', 'FRI']
    table = pd.DataFrame(index=time_list, columns=week_list)
    for j in range(len(class_name)):
        i_start = 0
        i_end = 0
        for i in range(len(table.index)):
            start = table.index[i].split('-')[0]
            end = table.index[i].split('-')[1]
            if (start_time[j] == start):
                i_start = i
            if (end_time[j].split(':')[0] == end.split(':')[0]) and (end_time[j].split(':')[1] == "20") and (
                    end.split(':')[1] == "30"):
                i_end = i
            if (end_time[j] == end):
                i_end = i
        ## locate the time range

        for i in range(i_start, i_end + 1):
            table[day[j]].iloc[i] = class_name[j]
    return table

class ChangeWin:
    def __init__(self, window, task, student):
        global size
        self.i=size
        self.upper = window
        self.window = Toplevel(window)
        change = str(int(800*self.i))+'x'+str(int(500*self.i))+'+'+str(int(800*self.i))+'+'+str(int(800*self.i))
        self.window.geometry(change)
        self.window.title("Change " + task)
        self.window.resizable(False, False)

        img = Image.open("images/changebg.png")
        img = img.resize((int(1000*self.i), int(600*self.i)), Image.ANTIALIAS)
        self.changebg =ImageTk.PhotoImage(img)
        self.bg = Button(self.window, image=self.changebg)
        self.bg.pack(fill='both', expand='yes')
        self.old_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.old_entry.place(x=int(80*self.i), y=int(80*self.i), width=int(500*self.i))
        self.old = Label(self.window, text="Old " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        self.old.place(x=int(50*self.i), y=int(80*self.i))
        self.new_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.new_entry.place(x=int(420*self.i), y=int(220*self.i), width=int(500*self.i))

        self.new = Label(self.window, text="New " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        self.new.place(x=int(50*self.i), y=int(220*self.i))
        img = Image.open("images/confirm.png")
        img = img.resize((int(400*self.i), int(122*self.i)), Image.ANTIALIAS)
        self.confirm = ImageTk.PhotoImage(img)
        self.confirml = Button(self.window, image=self.confirm, command=partial(self.SQLchange, task, student.username))
        self.confirml.place(x=int(300*self.i), y=int(400*self.i))
        self.window.mainloop()

    def SQLchange(self, attr, Id):
        old = self.old_entry.get()
        new = self.new_entry.get()
        # get pwd
        if attr == "email":
            attr = "`info.email_addr`"
            select = "SELECT {} FROM Student WHERE student_id={}".format(attr, Id)
            cursor.execute(select)
            result = cursor.fetchall()
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

            print(re.search(regex, new))
            if result[0][0] == old and re.search(regex, new) and new != old:
                new = "\'"+ new +"\'"
                update = "UPDATE Student SET `info.email_addr`= {} WHERE student_id={}".format(new, Id)
                cursor.execute(update)
                myconn.commit()
                self.window.destroy()
                success("change email", self.upper)

            else:
                failure("change email", self.window)

        if attr == "password":
            attr = "`password`"
            select = "SELECT {} FROM Student WHERE student_id={}".format(attr, Id)
            cursor.execute(select)
            result = cursor.fetchall()
            if result[0][0] == old and new != old:
                new = "\'"+ new +"\'"
                update = "UPDATE Student SET `password`= {} WHERE student_id={}".format(new, Id)
                cursor.execute(update)
                myconn.commit()
                self.window.destroy()
                success("change password", self.upper)
            else:
                failure("change password", self.window)

def home_win(Id):
    window = Tk()
    HomePage(window, Id)
    window.mainloop()

def TimeConverter(timestr):
    ftr = [3600,60,1]
    return sum([a*b for a, b in zip(ftr, map(int, timestr.split(':')))])

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

if __name__ == "__main__":
    # debuging purpose
    home_win(5)
