# This is new changes
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import ctypes
import time
from object import Student, Course, Deadline
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

ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="db")
cursor = myconn.cursor()
resizei = 0.4 #this factor is adjusted by different computer
resizee = 0.4

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
        self.i = resizei
        self.e = resizee
        self.materialsdb = dict()
        self.Id = Id
        self.current_panel = 2
        self.window = window
        self.window.geometry(str(int(3200*self.i))+"x"+str(int(2000*self.i))+"+300+0")
        self.window.title("HKU Student System")
        self.window.resizable(False, False)

        self.student = Student(Id)
        self.courses = Course(Id)

        style = ttk.Style(window)
        style.configure('lefttab.TNotebook', tabposition='wn')

        notebook = ttk.Notebook(window, style='lefttab.TNotebook')
        subframe1 = Image.open("images/subframe.png")
        self.subframe = ImageTk.PhotoImage(subframe1.resize((int(2480 * self.i), int(2001 * self.i)), Image.ANTIALIAS))
        self.f1 = Frame(notebook, width=int(2000*self.i), height=int(2000*self.i))
        self.f2 = Frame(notebook, width=int(2000*self.i), height=int(2000*self.i))
        self.f3 = Frame(notebook, width=2000*self.i, height=2000*self.i)
        self.f4 = Frame(notebook, width=2000*self.i, height=2000*self.i)

        img = Image.open("images/Profile.png")
        img = img.resize((int(700 * self.i), int(600 * self.i)), Image.ANTIALIAS)
        self.profile = ImageTk.PhotoImage(img)
        img = Image.open("images/courses.png")
        img = img.resize((int(700 * self.i), int(200 * self.i)), Image.ANTIALIAS)
        self.coursestab = ImageTk.PhotoImage(img)
        img = Image.open("images/timetable.png")
        img = img.resize((int(700 * self.i), int(200 * self.i)), Image.ANTIALIAS)
        self.timetable = ImageTk.PhotoImage(img)
        img = Image.open("images/deadline.png")
        img = img.resize((int(700 * self.i), int(200 * self.i)), Image.ANTIALIAS)
        self.deadline = ImageTk.PhotoImage(img)
        notebook.add(self.f1, text='Frame 1', image=self.profile)
        notebook.add(self.f2, text='Frame 2', image=self.timetable)
        notebook.add(self.f3, text='Frame 3', image=self.coursestab)
        notebook.add(self.f4, text='Frame 4', image=self.deadline)
        logoutb = Image.open('images/logout-05.png')
        logoutb1 = logoutb.resize((int(700 * self.i), int(200 * self.i)), Image.ANTIALIAS)
        self.logoutb = ImageTk.PhotoImage(logoutb1)
        self.Logout_button = Button(self.window, image = self.logoutb, command = self.logout)
        self.Logout_button.place(x = 0, y = int(self.i*1240))

        subf = Image.open('images/f1.png')
        subf1 = subf.resize((int(2500 * self.i), int(2000 * self.i)), Image.ANTIALIAS)
        self.subframe1 = ImageTk.PhotoImage(subf1)
        subf2 = Image.open('images/f2.png')
        subf2 = subf2.resize((int(2500 * self.i), int(2000 * self.i)), Image.ANTIALIAS)
        subf3 = Image.open('images/f3.png')
        subf3 = subf3.resize((int(2500 * self.i), int(2000 * self.i)), Image.ANTIALIAS)
        subf4 = Image.open('images/f4.png')
        subf4 = subf4.resize((int(2500 * self.i), int(2000 * self.i)), Image.ANTIALIAS)
        self.subframe2 = ImageTk.PhotoImage(subf2)
        self.subframe3 = ImageTk.PhotoImage(subf3)
        self.subframe4 = ImageTk.PhotoImage(subf4)
        self.image_panel = Label(self.f1, image=self.subframe1)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f2, image=self.subframe2)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f3, image=self.subframe3)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f4, image=self.subframe4)
        self.image_panel.pack(fill='both', expand='yes')

        ttF = Image.open('images/ttFrame.png')
        ttF1 = ttF.resize((int(1800 * self.i), int(1200 * self.i)), Image.ANTIALIAS)
        self.ttF = ImageTk.PhotoImage(ttF1)
        self.image_panel = Label(self.f2, image=self.ttF)
        self.image_panel.place(x=int(self.i*300), y=int(self.i*700))
        cg = Image.open('images/coursegrid.png')
        cg1 = cg.resize((int(1800 * self.i), int(250 * self.i)), Image.ANTIALIAS)
        self.coursegrid = ImageTk.PhotoImage(cg1)

        notebook.grid(row=0, column=0, sticky="nw")
        self.txt = "home page"
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", int(self.e*30), "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)

        self.name = self.student.name
        self.clabel = Label(self.window, text=self.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.clabel.place(x=int(self.i*170), y=int(self.i*380))

        self.clabel = Label(self.window, text="Current time", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.clabel.place(x=int(self.i*100), y=int(self.i*480))
        self.label = Label(self.window, text="", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", int(self.e*13), "bold"))
        self.update_clock()
        self.label.place(x=int(self.i*450), y=int(self.i*480))
        self.timetable2 = generateClassTable(self.student, self.courses)
        Img = Image.open('images/timegrid.png')
        tg = Img.resize((int(300 * self.i), int(100 * self.i)), Image.ANTIALIAS)
        self.timegrid = ImageTk.PhotoImage(tg)
        Img = Image.open('images/tutorialgrid.png')
        ttg = Img.resize((int(300 * self.i), int(100 * self.i)), Image.ANTIALIAS)
        self.tutorialgrid = ImageTk.PhotoImage(ttg)
        self.X = len(self.timetable2)
        self.Y = len(self.timetable2.columns)  # 5
        self.l_name = Label(self.f1, text=self.student.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.l_name.place(x=int(self.i*400), y=int(self.i*285))
        self.l_email = Label(self.f1, text=self.student.email_addr, bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", int(self.e*13), "bold"))
        self.l_email.place(x=int(self.i*500), y=int(self.i*585))
        self.l_user_id = Label(self.f1, text=self.student.username, bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", int(self.e*13), "bold"))
        self.l_user_id.place(x=int(self.i*500), y=int(self.i*385))
        self.l_year = Label(self.f1, text=self.student.admitted_year, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.l_year.place(x=int(self.i*600), y=int(self.i*485))
        self.login = Label(self.f1, text=str(self.student.login_date)+"   "+str(self.student.login_time), bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", int(self.e*13), "bold"))
        self.login.place(x=int(self.i*600), y=int(self.i*1585))
        self.logout = Label(self.f1, text=str(self.student.logout_date) +"   "+ str(self.student.logout_time) , bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.logout.place(x=int(self.i*600), y=int(self.i*1685))
        self.duration = Label(self.f1, text=self.student.duration, bg="white", fg="#4f4e4d",
                              font=("yu gothic ui", int(self.e*13), "bold"))
        self.duration.place(x=int(self.i*600), y=int(self.i*1785))

        Img = Image.open('images/changeemail.png')
        changee = Img.resize((int(656 * self.i), int(134 * self.i)), Image.ANTIALIAS)
        self.changee = ImageTk.PhotoImage(changee)
        self.changee_button = Button(self.f1, command=partial(self.change, "email", self.student), image=self.changee,
                                     relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.changee_button.place(x=int(self.i*100), y=int(self.i*740))

        Img = Image.open('images/changepw.png')
        changepw = Img.resize((int(656 * self.i), int(134 * self.i)), Image.ANTIALIAS)
        self.changepw = ImageTk.PhotoImage(changepw)
        self.changepw_button = Button(self.f1, image=self.changepw, command=partial(self.change, "password", self.student),
                                      relief=FLAT, borderwidth=0,
                                      cursor="hand2")
        self.changepw_button.place(x=int(self.i*850), y=int(self.i*740))
        self.notice = Label(self.f4, text="Deadline notification", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", int(self.e*13), "bold"))
        self.notice.place(x=int(self.i*100), y=int(self.i*400))
        self.CheckCourse(self.courses)
        customed_style = ttk.Style()
        customed_style.configure('Custom.TNotebook.Tab', padding=[int(self.i*12), int(self.i*12)], font=("yu gothic ui", int(self.e*12)))
        self.subnotebook = ttk.Notebook(self.f3, style='Custom.TNotebook')
        self.Lecture = Frame(self.subnotebook, bg="white", width=int(self.i*3000), height=int(self.i*2000))
        self.Tutorial = Frame(self.subnotebook, bg="white", width=int(self.i*3000), height=int(self.i*2000))
        self.subnotebook.add(self.Lecture, text='Lecture')
        self.subnotebook.add(self.Tutorial, text='Tutorial')
        self.subnotebook.place(x = int(self.i*0), y = int(self.i*200))
        self.filterTutorial()
        self.course_panel = []
        self.tutorial_panel = []
        self.tgrid = []
        self.lgrid = []
        for i in range(len(self.L)):
            m = i // 2
            n = i % 2
            cg = Image.open('images/coursegrid.png')
            Img = cg.resize((int(1100 * self.i), int(400 * self.i)), Image.ANTIALIAS)
            self.lgrid.append(ImageTk.PhotoImage(Img))
            self.course_panel.append(Button(self.Lecture, image=self.lgrid[i], command = partial(self.Coursewindow, self.L[i])))
            self.course_panel[i].place(x=int(self.i*80) + n * int(self.i*1200), y=int(self.i*100) + m * int(self.i*500))
            self.course_info1 = Label(self.Lecture, text=self.courses.course_name[self.L[i]],
                                      font=("yu gothic ui", int(12*self.e)))
            self.course_info1.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*130) + m * int(self.i*500))
            self.course_info2 = Label(self.Lecture, text=self.courses.course_long_name[self.L[i]],
                                      font=("yu gothic ui", int(12*self.e)))
            self.course_info2.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*200) + m * int(self.i*500))
            self.course_info3 = Label(self.Lecture, text="Instructor: " + self.courses.instructor[self.L[i]],
                                      font=("yu gothic ui", int(12*self.e)))
            self.course_info3.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*360) + m * int(self.i*500))

        for i in range(len(self.T)):
            m = i // 2
            n = i % 2
            cg = Image.open('images/coursegrid.png')
            Img = cg.resize((int(1100 * self.i), int(400 * self.i)), Image.ANTIALIAS)
            self.tgrid.append(ImageTk.PhotoImage(Img))
            self.tutorial_panel.append(Button(self.Tutorial, image=self.tgrid[i], command = partial(self.Coursewindow, self.T[i])))
            self.tutorial_panel[i].place(x=int(self.i*80) + n * int(self.i*1200), y=int(self.i*100) + m * int(self.i*500))
            self.course_info1 = Label(self.Tutorial, text=self.courses.course_name[self.T[i]], font=("yu gothic ui", int(self.e*12)))
            self.course_info1.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*130) + m * int(self.i*500))
            self.course_info2 = Label(self.Tutorial, text=self.courses.course_long_name[self.T[i]],font=("yu gothic ui", int(self.e*12)))
            self.course_info2.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*200) + m * int(self.i*500))
            self.course_info3 = Label(self.Tutorial, text="Instructor: " + self.courses.instructor[self.T[i]], font=("yu gothic ui", int(self.e*12)))
            self.course_info3.place(x=int(self.i*120) + n * int(self.i*1200), y=int(self.i*360) + m * int(self.i*500))

        self.update_clock()
        notebook.select(self.f2)

        for i in range(self.X):
            for j in range(self.Y):
                if (isinstance(self.timetable2.iloc[i, j], str)):
                    if  re.search("Tutorial", self.timetable2.iloc[i, j]):
                        self.tt = Label(self.f2, image=self.tutorialgrid, relief=FLAT, borderwidth=0,  cursor="hand2")
                        self.ttlabel = Label(self.f2, text=self.timetable2.iloc[i, j], font=("yu gothic ui", int(self.e*6), "bold"),
                                         bg="pale green")
                    else:
                        self.tt = Label(self.f2, image=self.timegrid, relief=FLAT, borderwidth=0,  cursor="hand2")
                        self.ttlabel = Label(self.f2, text=self.timetable2.iloc[i, j], font=("yu gothic ui", int(self.e*6), "bold"),
                                         bg="pale turquoise")
                    a = int(self.i*(600 + 300 * j))
                    b = int(self.i*(800 + 60 * (i - 1)))
                    self.tt.place(x=a, y=b)
                    self.ttlabel.place(x=a, y=b)

        self.deadlines = Deadline(Id)
        '''
        for i in range(len(self.deadlines.course_name)):
            self.notification = Label(self.f4, text=self.deadlines.course_name[i] +
                                                    ": " + self.deadlines.event[i]+" : will be due on " + str(self.deadlines.date[i].year) + "-" +
            str(self.deadlines.date[i].month) + "-" + str(self.deadlines.date[i].day) + " "+time_convert(
                self.deadlines.time[i]), bg = "white", fg = "#4f4e4d", font = ("yu gothic ui", 13, "bold"))
            self.notification.place(x=100, y= 400 + 200 * i)'''
        self.deadlineF = Frame(self.f4, width=int(self.i*2700), height=int(self.i*1500))
        self.deadlineF.place(x=0, y = int(self.i*300))
        canvas = Canvas(self.deadlineF)
        canvas.grid(row=0, column=0, sticky="news")
        sb = Scrollbar(self.deadlineF, orient="vertical", command=canvas.yview)
        sb.grid(row=0, column=1, sticky='ns')
        canvas.configure(width=int(self.i*2400), height = int(self.i*1500))
        canvas.configure(yscrollcommand=sb.set)
        frame_materials = Frame(canvas)
        canvas.create_window((0, 0), window=frame_materials, anchor='nw')
        i = 0;
        for i in range(len(self.deadlines.date)):
            self.mn = Button(frame_materials, text="     "+self.deadlines.course_name[i] +
                                                    ": " + self.deadlines.event[i]+" : will be due on " + str(self.deadlines.date[i].year) + "-" +
            str(self.deadlines.date[i].month) + "-" + str(self.deadlines.date[i].day) + " "+time_convert(
                self.deadlines.time[i]),font=("yu gothic ui", int(self.e*12), "bold"), bg="white", anchor="w", height= 3, width = int(self.i*180))
            self.mn.grid(row=i, column=0, sticky='news')
            i = i + 1;
        frame_materials.config(height= int(self.i*i*254))
        canvas.config(scrollregion=canvas.bbox("all"))
        success("login", self.window)

    def logout(self):
        self.updateduration()
        self.window.destroy()

    def updateduration(self):
        student_id = self.Id
        date = datetime.datetime.today()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cursor = myconn.cursor()
        select = "SELECT `login.time` FROM Student WHERE student_id={}".format(student_id)
        cursor.execute(select)
        result = cursor.fetchone()[0]
        duration = now - result
        update1 = "UPDATE Student SET `logout.date`=%s WHERE student_id=%s"
        val = (date, student_id)
        cursor.execute(update1, val)
        update = "UPDATE Student SET `logout.time`=%s WHERE student_id=%s"
        val2 = (current_time, student_id)
        cursor.execute(update, val2)
        update3 = "UPDATE Student SET `duration`=%s WHERE student_id=%s"
        val3 = (duration.strftime("%H:%M:%S"), student_id)
        cursor.execute(update3, val3)
        myconn.commit()
        self.window.destroy()
        success("logout", "")


    def Coursewindow(self, num):
        self.window2 = Toplevel(self.window)
        self.window2.geometry("")
        self.window2.title(self.courses.course_name[num]+"  "+ self.courses.course_long_name[num])
        self.window2.resizable()
        templist = self.materialsdb[self.courses.course_name[num]]
        print(templist)


        img = Image.open("images\\subcourse.png")
        img = img.resize((int(1809 * self.i), int(2016 * self.i)), Image.ANTIALIAS)
        self.f = ImageTk.PhotoImage(img)

        self.fw = Label(self.window2, image=self.f)
        self.fw.pack(fill='both', expand='yes')
        self.msg = Label(self.window2, text=self.courses.course_name[num]+"  "+ str(self.courses.course_long_name[num]),
                         font=("yu gothic ui", int(self.e*10), "bold"))
        self.msg.place(x=int(self.i*120), y=int(self.i*250))
        self.start_time = Label(self.window2, text="Instructor: " + str(self.courses.instructor[num]), font=("yu gothic ui", int(self.e*10), "bold"), bg = "white")
        self.start_time.place(x=int(self.i*120), y=int(self.i*600))
        self.duration_time = Label(self.window2, text="Office: "+str(self.courses.office[num]), font=("yu gothic ui", int(self.e*10), "bold"), bg = "white")
        self.duration_time.place(x=int(self.i*120), y=int(self.i*680))
        self.offHour = Label(self.window2, text= "Office Hour: " + str(self.courses.office_hour[num]), font=("yu gothic ui", int(self.e*10), "bold"), bg = "white")
        self.offHour.place(x=int(self.i*120), y=int(self.i*760))
        self.add = Label(self.window2, text="Site: " + str(self.courses.building_name[num]) + str(self.courses.room_number[num]),
                         font=("yu gothic ui", int(self.e*10), "bold"), bg="white")
        self.add.place(x=int(self.i*120), y=int(self.i*840))
        self.zoomlinkl = Label(self.window2, text="Zoom Link:",
                              font=("yu gothic ui", int(self.e*10), "bold"), bg="white")
        self.zoomlinkl.place(x= int(self.i*120), y=int(self.i*920))
        self.zoomlink = Message(self.window2, text=self.courses.zoom_link[num],
                             font=("yu gothic ui", int(self.e*10), "bold"), bg="white", width = 1200)
        self.zoomlink.place(x=int(self.i*110), y=int(self.i*1000))
        self.zoomlink.bind("<Button-1>", callback)
        self.mes = Label(self.window2,
                         text="Teacher's Message: " + str(self.courses.message[num]),
                         font=("yu gothic ui", int(self.e*10), "bold"), bg="white")
        self.mes.place(x=int(self.i*140), y=int(self.i*480))
        self.w2 = Frame(self.window2, width = int(self.i*2000), height = int(self.i*660))
        self.w2.place(x = 0, y = int(self.i*1300))
        canvas = Canvas(self.w2)
        canvas.grid(row=0, column=0, sticky="news")
        sb = Scrollbar(self.w2, orient="vertical", command=canvas.yview)
        sb.grid(row=0, column=1, sticky='ns')
        canvas.configure(width=int(self.i*1755), height = int(self.i*660))
        canvas.configure(yscrollcommand=sb.set)
        frame_materials = Frame(canvas, bg="blue")
        canvas.create_window((0, 0), window=frame_materials, anchor='nw')
        i = 0;
        k = 0;
        self.emailbuttons=[];
        self.emailb=[];
        for numk in templist:
            self.mn = Button(frame_materials, text="   "+"Material Name: "+str(self.courses.material_name[numk]),
                              font=("yu gothic ui", int(self.e*10), "bold"), bg="white", anchor="w", width = int(self.i*160))

            self.mn.grid(row=i, column=0, sticky='news')
            self.md = Button(frame_materials, text="   "+str(self.courses.material_date[numk]),
                          font=("yu gothic ui", int(self.e*10), "bold"), bg="white" , anchor="w", width = int(self.i*160))
            self.md.grid(row=i+1, column=0, sticky='news')
            self.dl = Button(frame_materials, text="   "+"Link: ",
                            font=("yu gothic ui", int(self.e*10), "bold"), bg="white", anchor="w", width = int(self.i*160))
            self.dl.grid(row=i+2, column=0, sticky='news')
            self.ml = Button(frame_materials, text="   "+str(self.courses.material_link[numk]),
                          font=("yu gothic ui", int(self.e*10), "bold"), bg="white", anchor="w", width = int(self.i*160))
            self.ml.grid(row=i+3, column=0, sticky='news')
            self.ml.bind("<Button-1>", callback)

            img = Image.open("images\\20-20.png")
            img = img.resize((int(960 * self.i), int(109 * self.i)), Image.ANTIALIAS)
            self.emailb.append(ImageTk.PhotoImage(img))

            self.emailbuttons.append(Button(frame_materials, image=self.emailb[k],
                                  command=partial(self.sendEmails, self.student, self.courses, numk, "")))
            self.emailbuttons[k].grid(row=i+4, column=0, sticky='news')
            i = i + 5;
            k = k+1;
        frame_materials.update_idletasks()
        frame_materials.config(height= int(self.i*i*100))
        canvas.config(scrollregion=canvas.bbox("all"))

    def remove_duplicate(self, T):
        db = dict()
        result = []
        for i in T:
            temp = db.get(self.courses.course_name[i], 'W')
            if temp == 'W':
                result.append(i)
                db[self.courses.course_name[i]] = i
            temp2 = self.materialsdb.get(self.courses.course_name[i], 'W')
            if temp2 == 'W':
                self.materialsdb[self.courses.course_name[i]] = []
                self.materialsdb[self.courses.course_name[i]].append(i)
            else:
                self.materialsdb[self.courses.course_name[i]].append(i)
        return result

    def filterTutorial(self):
        k = len(self.courses.course_type)
        self.T = []
        self.L = []
        for i in range(k):
            if self.courses.course_type[i] =="Tutorial":
                self.T.append(i)
            else:
                self.L.append(i)
        self.T = self.remove_duplicate(self.T)
        self.L = self.remove_duplicate(self.L)

    def change(self, task, student):
        ChangeWin(self.window, task, student)
        self.student = Student(self.Id)
        self.l_email = Label(self.f1, text=self.student.email_addr, bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", int(self.e*13), "bold"))

    def sendEmails(self, s, c, num, begin = "The following course will begin within an hour."):
        # send emails
        ## set up sender's account
        address = s.email_addr
        content = """Dear {0} ({1}):

{18}
The corresponding course materials are attached below for your reference.

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
                if (start.seconds - current <= 3599 ) and (start.seconds >= current):
                    flag = True
                    num = i
                    break
                elif (start.seconds+duration.seconds  >= current and start.seconds < current):
                    num = -i
                    flag = True
                    break
        if flag == True and num >= 0:
             upcoming = "You have class {} in one hour!\n Click the right button to send details to your email".format(course.course_name[num])
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


            img = Image.open("images\\haveclass.png")
            img = img.resize((int(1802 * self.i), int(252 * self.i)), Image.ANTIALIAS)
            self.haveclassbg = ImageTk.PhotoImage(img)

            self.haveclass = Label(self.f2, image=self.haveclassbg,
                                       relief=FLAT, borderwidth=0,
                                       cursor="hand2")
            self.haveclass.place(x=int(self.i*300), y=int(self.i*350))


            img = Image.open("images\\checkButton.png")
            img = img.resize((int(147 * self.i), int(148 * self.i)), Image.ANTIALIAS)
            self.checkButton = ImageTk.PhotoImage(img)

            self.check_button = Button(self.f2, image=self.checkButton, command=partial(self.sendEmails, self.student, self.courses, num),
                                       relief=FLAT, borderwidth=0,
                                       cursor="hand2")
            self.check_button.place(x=int(self.i*1900), y=int(self.i*400))
        else:

             img = Image.open("images\\noclass.png")
             img = img.resize((int(1802 * self.i), int(252 * self.i)), Image.ANTIALIAS)
             self.noclassbg = ImageTk.PhotoImage(img)

             self.noclass = Label(self.f2, image=self.noclassbg,
                                        relief=FLAT, borderwidth=0,
                                        cursor="hand2")
             self.noclass.place(x=int(self.i*300), y=int(self.i*350))
        self.msg = Label(self.f2, text = text, font=("yu gothic ui", int(self.e*13), "bold"))
        self.msg.place(x=int(self.i*400), y = int(self.i*400))

    def display_course(self, window, courses, num, i):
        m = i//2
        n = i % 2


        img = Image.open("images\\coursegrid.png")
        img = img.resize((int(1102 * self.i), int(401 * self.i)), Image.ANTIALIAS)
        self.coursegrid = ImageTk.PhotoImage(img)

        self.image_panel = Button(window, image=self.coursegrid, command=partial(self.Coursewindow, courses, num))
        self.image_panel.place(x=int(self.i*(80+n*1200)), y=int(self.i*(400 + m*500)))
        self.course_info = Label(window, text = courses.course_name[num] )
        self.course_info.place(x=int(self.i*(90 + n * 1200)), y=int(self.i*(410 + m * 500)))
        self.course_info = Label(window, text=courses.instructor[num])
        self.course_info.place(x=int(self.i*(90 + n * 1200)), y=int(self.i*470 + m * 500))

class successWin:
    def __init__(self, task, window):
        self.i = resizei;
        self.e = resizee;
        if (task == "logout"):
            self.window = Tk()
        else:
            self.window = Toplevel(window)
        self.txt = "Successfully " + task
        self.window.geometry(str(int(800 * self.i)) + "x" + str(int(500 * self.i)) + "+400+400")
        self.window.title("success!")
        img = Image.open("images\\successbg.png")
        img = img.resize((int(800 * self.i), int(501 * self.i)), Image.ANTIALIAS)
        self.successbg = ImageTk.PhotoImage(img)

        self.bg = Button(self.window, image=self.successbg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", int(self.e*10), "bold"))
        self.msg.place(x=int(self.i*80), y=int(self.i*200))
        self.window.attributes('-topmost', 'true')

def success(task,window):
    S = successWin(task, window)
    S.window.after(3000, lambda: S.window.destroy())
    S.window.mainloop()

class FailureWin:
    def __init__(self, task, window):
        self.i = resizei
        self.e = resizee
        self.txt = "Problems: unable to " + task+", \nyou need to check your input."
        self.window = Toplevel(window)
        self.window.geometry(str(int(800*self.i))+"x"+str(int(500*self.i))+"+400+400")
        self.window.title("Warning!")


        img = Image.open("images\\failurebg.png")
        img = img.resize((int(801 * self.i), int(501 * self.i)), Image.ANTIALIAS)
        self.failurebg = ImageTk.PhotoImage(img)

        self.bg = Button(self.window, image=self.failurebg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", int(self.e*10), "bold"))
        self.msg.place(x=int(self.i*80), y=int(self.i*200))
        self.window.mainloop()

def failure(task,window):
    S = FailureWin(task, window)
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
        self.i = resizei
        self.e = resizee
        self.upper = window
        self.window = Toplevel(window)
        self.window.geometry(str(int(1000*self.i))+"x"+str(int(600*self.i))+"+300+300")
        self.window.title("Change " + task)
        self.window.resizable(False, False)

        img = Image.open("images\\changebg.png")
        img = img.resize((int(1001 * self.i), int(601 * self.i)), Image.ANTIALIAS)
        self.changebg = ImageTk.PhotoImage(img)

        self.bg = Button(self.window, image=self.changebg)
        self.bg.pack(fill='both', expand='yes')
        self.old_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", int(self.e*12)))
        self.old_entry.place(x=int(self.i*420), y=int(self.i*80), width=int(self.i*500))
        self.old = Label(self.window, text="Old " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", int(self.e*13), "bold"))
        self.old.place(x=int(self.i*50), y=int(self.i*80))
        self.new_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", int(self.e*12)))
        self.new_entry.place(x=int(self.i*420), y=int(self.i*220), width=int(self.i*500))

        self.new = Label(self.window, text="New " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", int(self.e*13), "bold"))
        self.new.place(x=int(self.i*50), y=int(self.i*220))


        img = Image.open("images\\confirm.png")
        img = img.resize((int(401 * self.i), int(122 * self.i)), Image.ANTIALIAS)
        self.confirm = ImageTk.PhotoImage(img)

        self.confirml = Button(self.window, image=self.confirm, command=partial(self.SQLchange, task, student.username))
        self.confirml.place(x=int(self.i*300), y=int(self.i*400))
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

def ReverseConvert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d:%02d" % (hour, minutes, seconds)

def TimeConverter(timestr):
    ftr = [3600,60,1]
    return sum([a*b for a, b in zip(ftr, map(int, timestr.split(':')))])

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

if __name__ == "__main__":
    home_win(5)
