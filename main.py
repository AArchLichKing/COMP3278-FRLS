# This is a sample Python script.
from tkinter import *
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import random
import datetime, time
import os
import random
import cv2
from faceCapture import faceCapture
from train import train

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

#myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="facerecognition")
#cursor = myconn.cursor()

class ConnectDatabase:
    def __init__(self, window):
        self.window = window
        self.window.geometry("3200x2000+100+50")
        self.window.title("HKU Student System")
        self.window.resizable(False,False)
        self.database_frame = ImageTk.PhotoImage\
            (file='images\\frame.png')
        self.image_panel = Label(self.window, image=self.database_frame)
        self.image_panel.pack(fill='both', expand='yes')
        self.txt = "HKU Student System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", 30, "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=200, width=2400)
        self.slider()
        self.heading_color()

        self.username_label = Label(self.window, text="Username", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=1800, y=560)

        self.username_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=2200, y=568, width=800)

        # ==================Password Label and Entry==================
        self.password_label = Label(self.window, text="Password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=1800, y=720)

        self.password_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=2200, y=728, width=800)
        
        def autoSignIn():
            now = time.time()  ###For calculate seconds of video
            future = now + 20
            
            #record sign in time
            global ts
            global date
            global timeStamp
            
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            
            if time.time() < future:
            
                recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel\Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                harcascadePath = "haarcascade\haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                font = cv2.FONT_HERSHEY_SIMPLEX
                
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf <70):
                            #Is registered student
                            print(conf)
                            global date1
                            global timeStamp1
                            ts = time.time()
                            date1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp1 = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            global tt
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)                        
                            #open main page according to Id
                            
                        else:
                            Id = 'Unknown'
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break
                    
                    cv2.imshow('Checking Identity..', im)
                    key = cv2.waitKey(30) & 0xff
                    if key == 27:
                        break
                        
                cam.release()
                cv2.destroyAllWindows()

        def manuallySignIn():
            #record sign in time
            global ts
            global date
            global timeStamp
            
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            
            #read username from blank
            username = self.username_entry.get()
            
            #get pwd
            select = "SELECT pwd FROM Student WHERE username='%s'" % (username)
            name = cursor.execute(select)
            result = cursor.fetchall()            
                       
            #compare with corresponding pwd            
            match = result == self.password_entry.get()            
            if match:
                #open main page
                pass
            else:
                #generate err message
                e = 'Wrong pwd!'
                Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

        def Register():            
            #read username from blank
            username = self.register_username_entry.get()
            pwd = self.register_password_entry.get()
            
            #capture photos of user
            faceCapture(username)
            
            #save username, pwd to database
            insert = '' #sql query of insert
            cursor.execute(insert)
            
            if True:
                #train new model with data
                train()

        self.submit = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.submit_button = Button(self.window, image=self.submit, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.submit_button.place(x=1800, y=940)

        self.face= ImageTk.PhotoImage \
            (file='images\\face.png')
        self.face_button = Button(self.window, command=autoSignIn, image=self.face, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.face_button.place(x=2660, y=940)
        
        Notifica = tk.Label(self.window, text="", bg="Green", fg="white", width=33,
                            height=2, font=('times', 15, 'bold'))

        # ============Placing Button============
        self.login = ImageTk.PhotoImage \
            (file='images\\Register.png')

        self.login_button = Button(self.window,command=manuallySignIn ,image=self.login, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.login_button.place(x=1800, y=1350)

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

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

def win():
    window = Tk()
    ConnectDatabase(window)
    window.mainloop()

win()