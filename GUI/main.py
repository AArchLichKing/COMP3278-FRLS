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

class ConnectDatabase:
    def __init__(self, window):
        self.window = window
        self.window.geometry("800x500+100+50")
        self.window.title("HKU Student System")
        # self.window.iconbitmap('images/icon.ico')
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
        self.heading.place(x=100, y=50, width=600)
        self.slider()
        self.heading_color()

        self.username_label = Label(self.window, text="Username", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=450, y=140)

        self.username_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.username_entry.place(x=550, y=142, width=200)

        # ==================Password Label and Entry==================
        self.password_label = Label(self.window, text="Password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=450, y=180)

        self.password_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", 12))
        self.password_entry.place(x=550, y=182, width=200)
        
        def autoSignIn():
            now = time.time()  ###For calculate seconds of video
            future = now + 20
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
                            global date
                            global timeStamp
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
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
            
            #connect database
            
            #read username from blank
            
            #compare with corresponding pwd
            
            match = True
            if match:
                #open main page
                pass
            else:
                #generate err message
                pass

        # ============Placing Button============
        def Register():            
            #read username from blank
            faceCapture(username)
            #save username, pwd to database
            
            if True:
                #train new model with data
                train()

        self.submit = ImageTk.PhotoImage \
            (file='images\\submit.png')

        self.submit_button = Button(self.window, image=self.submit, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.submit_button.place(x=450, y=240)
        # ============Placing Button============
        self.face= ImageTk.PhotoImage \
            (file='images\\face.png')

        self.face_button = Button(self.window, command=autoSignIn, image=self.face, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.face_button.place(x=640, y=240)
        
        Notifica = tk.Label(self.window, text="Attendance filled Successfully", bg="Green", fg="white", width=33,
                            height=2, font=('times', 15, 'bold'))

        # ============Placing Button============
        self.login = ImageTk.PhotoImage \
            (file='images\\Register.png')

        self.login_button = Button(self.window, image=self.login, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.login_button.place(x=450, y=340)

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