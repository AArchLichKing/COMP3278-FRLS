# This is a sample Python script.
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkintertable import TableCanvas, TableModel
import ctypes
import time
from object import Student, Course
import mysql.connector
from functools import partial
import re
import datetime

import smtplib
from email.mime.text import MIMEText
## import packages for send_email()
import pandas as pd

## import packages for generateClassTable()

ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="db")
cursor = myconn.cursor()


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
        self.Id = Id
        self.current_panel = 2
        self.window = window
        self.window.geometry("3200x2000+200+100")
        self.window.title("HKU Student System")
        self.window.resizable(False, False)

        self.student = Student(4)
        self.courses = Course(4)
        '''
        I wish to extract the first course name:
        course.name[0]
        course.time[0]
        
        I wish to extract the second course name:
        course.name[1]
        course.time[1]
        
        for i in range(len(course.name)):
        '''

        style = ttk.Style(window)
        style.configure('lefttab.TNotebook', tabposition='wn')

        notebook = ttk.Notebook(window, style='lefttab.TNotebook')
        self.subframe = ImageTk.PhotoImage \
            (file='images\\subframe.png')

        self.f1 = Frame(notebook, bg="white")
        self.f2 = Frame(notebook, width=2000, height=2000)
        self.f3 = Frame(notebook, width=2000, height=2000)
        self.f4 = Frame(notebook, width=2000, height=2000)

        self.profile = ImageTk.PhotoImage \
            (file='images\\Profile.png')
        self.coursestab = ImageTk.PhotoImage \
            (file='images\\courses.png')
        self.timetable = ImageTk.PhotoImage \
            (file='images\\timetable.png')
        self.deadline = ImageTk.PhotoImage \
            (file='images\\deadline.png')
        notebook.add(self.f1, text='Frame 1', image=self.profile)
        notebook.add(self.f2, text='Frame 2', image=self.timetable)
        notebook.add(self.f3, text='Frame 3', image=self.coursestab)
        notebook.add(self.f4, text='Frame 4', image=self.deadline)
        self.subframe = ImageTk.PhotoImage \
            (file='images\\subframe.png')
        self.subframe1 = ImageTk.PhotoImage \
            (file='images\\f1.png')
        self.image_panel = Label(self.f1, image=self.subframe1)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f2, image=self.subframe)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f3, image=self.subframe)
        self.image_panel.pack(fill='both', expand='yes')
        self.image_panel = Label(self.f4, image=self.subframe)
        self.image_panel.pack(fill='both', expand='yes')
        self.ttF = ImageTk.PhotoImage \
            (file='images\\ttFrame.png')
        self.image_panel = Label(self.f2, image=self.ttF)
        self.image_panel.place(x=300, y=700)
        self.coursegrid = ImageTk.PhotoImage \
            (file='images\\coursegrid.png')
        




        """
        self.image_panel = Button(f3, image=self.coursegrid, command=partial(self.Coursewindow, self.courses, 0))
        self.image_panel.place(x=80, y=400)
        self.image_panel = Button(f3, image=self.coursegrid, command=partial(self.Coursewindow, self.courses, 0))
        self.image_panel.place(x=1280, y=400)
        self.image_panel = Button(f3, image=self.coursegrid, command=partial(self.Coursewindow, self.courses, 0))
        self.image_panel.place(x=80, y=900)
        self.image_panel = Button(f3, image=self.coursegrid, command=partial(self.Coursewindow, self.courses, 0))
        self.image_panel.place(x=1280, y=900)
        self.image_panel = Button(f3, image=self.coursegrid)
        self.image_panel.place(x=1280, y=1400)
        self.image_panel = Button(f3, image=self.coursegrid)
        self.image_panel.place(x=80, y=1400)    """

        notebook.grid(row=0, column=0, sticky="nw")
        self.txt = "home page"
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", 30, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)

        self.name = self.student.name
        self.clabel = Label(self.window, text=self.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=170, y=380)

        self.clabel = Label(self.window, text="Current time", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.clabel.place(x=100, y=480)
        self.label = Label(self.window, text="", bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.update_clock()
        self.label.place(x=450, y=480)
        self.timetable2 = generateClassTable(self.student, self.courses)
        self.timegrid = ImageTk.PhotoImage(file='images\\timegrid.png')
        self.tutorialgrid = ImageTk.PhotoImage(file='images\\tutorialgrid.png')
        self.X = len(self.timetable2)
        self.Y = len(self.timetable2.columns)  # 5
        self.l_name = Label(self.f1, text=self.student.name, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.l_name.place(x=400, y=285)
        self.l_email = Label(self.f1, text=self.student.email_addr, bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", 13, "bold"))
        self.l_email.place(x=500, y=585)
        self.l_user_id = Label(self.f1, text=self.student.username, bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.l_user_id.place(x=500, y=385)
        self.l_year = Label(self.f1, text=self.student.admitted_year, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.l_year.place(x=600, y=485)
        self.login = Label(self.f1, text=self.student.last_login, bg="white", fg="#4f4e4d",
                           font=("yu gothic ui", 13, "bold"))
        self.login.place(x=600, y=1685)
        self.logout = Label(self.f1, text=self.student.last_logout, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.logout.place(x=600, y=1585)
        self.duration = Label(self.f1, text=self.student.duration, bg="white", fg="#4f4e4d",
                              font=("yu gothic ui", 13, "bold"))
        self.duration.place(x=600, y=1785)
        self.changee = ImageTk.PhotoImage \
            (file='images\\changeemail.png')
        self.changee_button = Button(self.f1, command=partial(self.change, "email", self.student), image=self.changee,
                                     relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.changee_button.place(x=100, y=740)
        self.changepw = ImageTk.PhotoImage \
            (file='images\\changepw.png')
        self.changepw_button = Button(self.f1, image=self.changepw, command=partial(self.change, "password", self.student),
                                      relief=FLAT, borderwidth=0,
                                      cursor="hand2")
        self.changepw_button.place(x=850, y=740)
        self.notice = Label(self.f4, text="Deadline notification", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.notice.place(x=100, y=80)
        self.notice2 = Label(self.f4, text="Deadline notification", bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.notice2.place(x=100, y=80)
        self.CheckCourse(self.courses)

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

                    a = 600 + 300 * j        
                    b = 800 + 60 * (i - 1)
                    self.tt.place(x=a, y=b)
                    self.ttlabel.place(x=a, y=b)

    def Coursewindow(self, course, num):
        self.window2 = Toplevel(self.window)
        self.window2.geometry("")
        self.window2.title("success!")
        self.window2.resizable()
        self.f = ImageTk.PhotoImage \
            (file='images\\subcourse.png')
        self.fw = Label(self.window2, image=self.f)
        self.fw.pack(fill='both', expand='yes')
        self.msg = Label(self.window2, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        self.msg.place(x=20, y=200)
        action_with_arg = partial(self.sendEmails, self.student, self.courses, 0)
        self.email = ImageTk.PhotoImage \
            (file='images\\20-20.png')
        self.email_b = Button(self.window2, image=self.email,
                              command=partial(self.sendEmails, self.student, self.courses, 0))
        self.email_b.place(x=20, y=1800)

    def change(self, task, student):
        ChangeWin(self.window, task, student)
        self.student = Student(self.Id)

    def sendEmails(self, s, c, num):
        # send emails
        ## set up sender's account
        num = 0
        address = "maoqi@connect.hku.hk"
        content = """Dear {0} ({1}):

    The following course will begin within an hour. The corresponding course materials are attached below for your reference.

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
                   c.message[num], c.course_long_name[num])

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

        success("send the emails!")

    def CheckCourse(self, course):
        now = time.strftime("%H:%M:%S")
        now = time.strftime("%H:%M:%S")
        current = TimeConverter(now)
        today = 1 #datetime.datetime.today().weekday()
        flag = False
        num = 0
        for i in range(len(course.start_time)):
            start = course.start_time[i]
            weekday = course.weekday[i]
            duration = course.duration[i]
            D = ["MON", "TUE","WED","THU","FRI"]
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
             self.msg(upcoming,1)
        elif flag:
             current = "You are currently taking {}! \n Click the right button to send details to your email".format(course.course_name[-num])
             self.msg(current,1)
        else:
             self.msg("No courses in ten minutes, check timetable for details",0)


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

    def msg(self, text, y):
        if y == 1:
            self.haveclassbg = ImageTk.PhotoImage \
                           (file='images\\haveclass.png')
            self.haveclass = Label(self.f2, image=self.haveclassbg,
                                       relief=FLAT, borderwidth=0,
                                       cursor="hand2")
            self.haveclass.place(x=300, y=350)
            self.checkButton = ImageTk.PhotoImage \
                           (file='images\\checkButton.png')
            self.check_button = Button(self.f2, image=self.checkButton, command=partial(self.sendEmails, self.student, self.courses, 0),
                                       relief=FLAT, borderwidth=0,                                                                                 
                                       cursor="hand2")                                                                                             
            self.check_button.place(x=1900, y=400)
        else:
             self.noclassbg = ImageTk.PhotoImage \
                            (file='images\\noclass.png')
             self.noclass = Label(self.f2, image=self.noclassbg,
                                        relief=FLAT, borderwidth=0,
                                        cursor="hand2")
             self.noclass.place(x=300, y=350)
        self.msg = Label(self.f2, text = text, font=("yu gothic ui", 13, "bold"))
        self.msg.place(x=400, y = 400)                       

class successWin:
    def __init__(self, task, window):
        self.txt = "Successfully " + task
        self.window = Toplevel(window)
        self.window.geometry("800x500+800+800")
        self.window.title("success!")
        self.successbg =ImageTk.PhotoImage \
                      (file='images\\successbg.png')
        self.bg = Button(self.window, image=self.successbg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 10, "bold"))
        self.msg.place(x=80, y=200)
        self.window.mainloop()

def success(task,window):
    S = successWin(task, window)
    S.window.mainloop()


class FailureWin:
    def __init__(self, task, window):
        self.txt = "Problems: unable to " + task+", \nyou need to check your input."
        self.window = Toplevel(window)
        self.window.geometry("800x500+800+800")
        self.window.title("Warning!")
        self.failurebg =ImageTk.PhotoImage \
                      (file='images\\failurebg.png')
        self.bg = Button(self.window, image=self.failurebg)
        self.bg.pack(fill='both', expand='yes')
        self.window.resizable(False, False)
        self.msg = Label(self.window, text=self.txt, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 10, "bold"))
        self.msg.place(x=80, y=200)
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
        self.upper = window
        self.window = Toplevel(window)
        self.window.geometry("1000x600+800+800")
        self.window.title("Change " + task)
        self.window.resizable(False, False)
        self.changebg =ImageTk.PhotoImage \
                      (file='images\\changebg.png')
        self.bg = Button(self.window, image=self.changebg)
        self.bg.pack(fill='both', expand='yes')
        self.old_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.old_entry.place(x=420, y=80, width=500)
        self.old = Label(self.window, text="Old " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        self.old.place(x=50, y=80)
        self.new_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12))
        self.new_entry.place(x=420, y=220, width=500)

        self.new = Label(self.window, text="New " + task, bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        self.new.place(x=50, y=220)
        self.confirm = ImageTk.PhotoImage \
            (file='images\\confirm.png')
        self.confirml = Button(self.window, image=self.confirm, command=partial(self.SQLchange, task, student.username))
        self.confirml.place(x=300, y=400)
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
                success("change password")
            else:
                failure("change password")

def home_win(Id):
    window = Tk()
    Id = 0
    HomePage(window, Id)
    window.mainloop()

def TimeConverter(timestr):
    ftr = [3600,60,1]
    return sum([a*b for a,b in zip(ftr, map(int, timestr.split(':')))])


if __name__ == "__main__":
    # debuging purpose
    home_win(4)