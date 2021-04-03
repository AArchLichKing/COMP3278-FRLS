# This is a sample Python script.
from tkinter import *
from tkinter import *
from PIL import Image,ImageTk
from tkintertable import TableCanvas, TableModel
import ctypes
import time
import mysql.connector

import smtplib
from email.mime.text import MIMEText
## import packages for send_email()
import pandas as pd
## import packages for generateClassTable()

ctypes.windll.shcore.SetProcessDpiAwareness(1)
import random

myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="facerecognition")
cursor = myconn.cursor()

def time_convert(time):
    ## Used to transform timedelta format to hr:minute:second
    seconds = time.seconds
    hour = str(seconds // 3600)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str((seconds//60)%60)
    if len(minute) == 1:
        minute = "0" + minute
    second = str(seconds%60)
    if len(second) == 1:
        second = "0" + second
    return hour + ":" + minute + ":" + second

class HomePage:
    def __init__(self, window, Id):
        self.current_panel = 2
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

        self.deadline_button.place(x=0, y=1000)
        if (self.current_panel == 1):
            self.Timetable()
        if (self.current_panel == 2):
            self.Courses()

    def Timetable(self):
        self.deadline2 = ImageTk.PhotoImage \
            (file='images\\deadline.png')
        self.deadline_button2 = Button(self.window, command=self.deadline2, image=self.deadline, relief=FLAT,
                                       borderwidth=0,
                                       cursor="hand2")

        self.deadline_button2.place(x=1000, y=1000)

    def connectDB():
        pass
    
    def generateMessage():
        #generate latest messages
        pass 
    
    def sendEmails(self, student, course):
        #send emails
        ## set up sender's account
        num = 0
        address = student.email_addr
        content = """Dear {0} ({1}):

    The following course will begin within an hour. The corresponding course materials are attached below for your reference.

        Course name: {2}
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

    Please check the course information and rememeber to take your course on time.

    Best regards,
    eLearning Team
        """.format(student.name, student.email_addr, course.course_name[num], course.course_type[num], course.weekday[num], time_convert(course.start_time[num]), time_convert(course.start_time[num]+course.duration[num]), course.building_name[num], course.room_number[num], course.zoom_link[num], course.material_name[num], course.material_date[num], course.material_link[num], course.instructor[num], course.office[num], course.office_hour[num])

        mail_host = 'smtp.163.com'
        mail_user = 'comp3278_group2'
        mail_pass = 'UGQEGXIPKFFLNHEQ'
        sender = 'comp3278_group2@163.com'
        receiver = [address]

        ## set up email information
        message = MIMEText(content,'plain','utf-8')
        message['Subject'] = 'HKU Course Notices'
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receiver)

        ## send email
        smtp0bj = smtplib.SMTP_SSL(mail_host,465)
        smtp0bj.login(mail_user,mail_pass)
        smtp0bj.sendmail(sender,receiver,message.as_string())
        smtp0bj.quit()
        success("Emails sent successfully!")

    def profile(self):

        pass

    def timetable(self):

        pass
    def Courses(self):

        coursename = "COMP3278, Section 2B, 2020"
        coursetacher = "Teacher" + "Luo Ping"
        self.coursegrid = ImageTk.PhotoImage \
            (file='images\\coursegrid.png')
        self.courses_button = Button(self.window, command=self.window.destroy, image=self.coursegrid, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.courses_button.place(x = 800, y = 600)
        self.tlabel = Label(self.window, text=coursename, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.tlabel.place(x=800, y=600)
        self.teacherlabel = Label(self.window, text=coursename, bg="white", fg="#4f4e4d",
                            font=("yu gothic ui", 13, "bold"))
        self.teacherlabel.place(x=800, y=700)


    def courses(self):
        self.coursegrid = ImageTk.PhotoImage \
            (file='images\\coursegrid.png')
        self.courses_button = Button(self.window, command=self.courses, image=self.courses, relief=FLAT, borderwidth=0,
                                     cursor="hand2")
        self.courses_button.place(x=1000, y=800)
        self.window.mainloop()

    def generateClassTable(self, class_name, start_time, end_time, day):
        #generate class table
        # class_name, start_time and end_time are lists containing each course's information
        time_list = ["9:00-9:30","9:30-10:00","10:00-10:30","10:30-11:00","11:00-11:30","11:30-12:00","12:00-12:30","12:30-13:00","13:00-13:30","13:30-14:00","14:00-14:30","14:30-15:00","15:00-15:30","15:30-16:00","16:00-16:30","16:30-17:00","17:00-17:30","17:30-18:00","18:00-18:30"]
        week_list = ['Monday','Tuesday','Wednesday','Thursday','Friday']
        table = pd.DataFrame(index = time_list,columns = week_list)
        for j in range(len(class_name)):
            i_start = 0
            i_end = 0
            for i in range(len(table.index)):
                start = table.index[i].split('-')[0]
                end = table.index[i].split('-')[1]
                if (start_time[j] == start):
                    i_start = i
                if (end_time[j] == end):
                    i_end = i
            ## locate the time range

            for i in range(i_start,i_end+1):
                table.iloc[i,day[j]] = class_name[j]

        ## transformation
        data = dict()
        for i in range(len(time_list)):
            data[time_list[i]] = dict()
            data[time_list[i]]['label'] = time_list[i]
            for j in range(len(week_list)):
                data[time_list[i]][week_list[j]] = table.iloc[i,j]

        tframe = Frame(master)
        tframe.pack()
        table = TableCanvas(tframe, data = data)
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

def home_win(Id):
    window = Tk()
    Id = 0
    HomePage(window, Id)
    window.mainloop()

#test function for success windows
def testSuc(filepath):
    success("send to your emails!", filepath)

if __name__ == "__main__":
  #debuging purpose
  home_win(1)
#file = "images\\Success\\email.png"
#testSuc(file)
