from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from homePage import home_win
import datetime, time
import random
import cv2, os
from faceCapture import faceCapture
from train import train
import mysql.connector
import ctypes
from homePage import success, failure

ctypes.windll.shcore.SetProcessDpiAwareness(1)
myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="db")
cursor = myconn.cursor()

class ConnectDatabase:
    def __init__(self, window):
        self.i=0.4
        self.window = window
        self.window = window
        change = str(int(3201*self.i))+'x'+str(int(2001*self.i))+'+' + str(int(200*self.i)) + '+' + str(int(100*self.i))
        self.window.geometry(change)
        self.window.title("HKU Student System")
        self.window.resizable(False, False)

        img = Image.open("images\\frame.png")
        img = img.resize((int(3200*self.i), int(2000*self.i)), Image.ANTIALIAS)
        self.database_frame = ImageTk.PhotoImage(img)

        self.image_panel = Label(self.window, image=self.database_frame)
        self.image_panel.pack(fill='both', expand='yes')
        self.txt = "HKU Student System"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.window, text=self.txt, font=("yu gothic ui", int(self.i*30), "bold"), bg="white", fg="black",
                             bd=5, relief=FLAT)
        self.heading.place(x=400*self.i, y=200*self.i, width=2400*self.i)
        self.slider()
        self.heading_color()

        self.username_label = Label(self.window, text="User_id", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", int(self.i*13), "bold"))
        self.username_label.place(x=1800*self.i, y=560*self.i)

        self.username_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", int(self.i*12)))
        self.username_entry.place(x=2200*self.i, y=568*self.i, width=800*self.i)

        # ==================Password Label and Entry==================
        self.password_label = Label(self.window, text="Password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", int(self.i*13), "bold"))
        self.password_label.place(x=1800*self.i, y=720*self.i)

        self.password_entry = Entry(self.window, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                    font=("yu gothic ui semibold", int(self.i*12)))
        self.password_entry.place(x=2200*self.i, y=728*self.i, width=800*self.i)

        img = Image.open("images\\login.png")
        img = img.resize((int(764*self.i), int(320*self.i)), Image.ANTIALIAS)
        self.submit = ImageTk.PhotoImage(img)

        self.submit_button = Button(self.window, command=self.manuallySignIn, image=self.submit, relief=FLAT,
                                    borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.submit_button.place(x=1800*self.i, y=1340*self.i)

        img = Image.open("images\\face.png")
        img = img.resize((int(323*self.i), int(324*self.i)), Image.ANTIALIAS)
        self.face = ImageTk.PhotoImage(img)

        self.face_button = Button(self.window, command=self.autoSignIn, image=self.face, relief=FLAT, borderwidth=0,
                                  background="white",
                                  activebackground="white", cursor="hand2")
        self.face_button.place(x=2660*self.i, y=1340*self.i)

        self.Notifica = tk.Label(self.window, text="", bg="Green", fg="white", width=int(self.i*33),
                                 height=2, font=('times', int(self.i*15), 'bold'))

        # ============Placing Button============
        img = Image.open("images\\Register.png")
        img = img.resize((int(1178*self.i), int(320*self.i)), Image.ANTIALIAS)
        self.register_img = ImageTk.PhotoImage(img)

        self.login_button = Button(self.window, command=self.register, image=self.register_img, relief=FLAT,
                                   borderwidth=0, background="white",
                                   activebackground="white", cursor="hand2")
        self.login_button.place(x=1800*self.i, y=920*self.i)

    def autoSignIn(self):
        now = time.time()  ###For calculate seconds of video
        future = now + 20
        login_flag = 0
        best_conf = 70
        # record sign in time
        global ts
        global date
        global timeStamp

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

        if time.time() < future:

            recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
            try:
                recognizer.read("TrainingImageLabel\Trainer_3.yml")
            except:
                e = 'Model not found or corrupted,Please train the model by clicking Register New Student'
                self.Notifica.configure(text=e, bg="red", fg="black", width=int(self.i*33), font=('times', int(self.i*15), 'bold'))
                self.Notifica.place(x=20*self.i, y=250*self.i)

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
                    tmp_Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

                    if conf < best_conf:
                        Id = tmp_Id
                        best_conf = conf

                    if (conf < 70):
                        # Is registered student
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        global tt
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)
                        # open main page according to Id, close login page
                        login_flag += 1
                    else:
                        Id = 'Unknown'
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                if time.time() > future:
                    break

                cv2.imshow('Checking Identity..', im)
                key = cv2.waitKey(10) & 0xff
                if key == 27 or login_flag > 30:
                    break

            cam.release()
            cv2.destroyAllWindows()

            if login_flag > 20:
                self.window.destroy()
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                image_dir = os.path.join(BASE_DIR, "data")
                label = os.listdir(image_dir)
                Id = label[Id]
                student_id = Id
                date = datetime.datetime.utcnow()
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                update = "UPDATE Student SET `login.date`=%s WHERE student_id=%s"
                val = (date, student_id)
                cursor.execute(update, val)
                update = "UPDATE Student SET `login.time`=%s WHERE student_id=%s"
                val = (current_time, student_id)
                cursor.execute(update, val)
                myconn.commit()
                home_win(Id)

    def manuallySignIn(self):
        # record sign in time
        global ts
        global date
        global timeStamp

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

        # read username from blank
        Id = self.username_entry.get()

        # get pwd
        select = "SELECT password FROM Student WHERE student_id='%s'" % (Id)
        name = cursor.execute(select)
        result = cursor.fetchall()

        # compare with corresponding pwd
        match = result[0][0] == self.password_entry.get()
        if match:
            # open main page according to Id, close login page
            self.window.destroy()
            student_id = Id
            date = datetime.datetime.utcnow()
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            update = "UPDATE Student SET `login.date`=%s WHERE student_id=%s"
            val = (date, student_id)
            cursor.execute(update, val)
            update = "UPDATE Student SET `login.time`=%s WHERE student_id=%s"
            val = (current_time, student_id)
            cursor.execute(update, val)
            myconn.commit()
            home_win(Id)

        else:
            # generate err message
            e = 'You are not legal student! Please input right username' if result == [] else 'Wrong pwd!'
            self.Notifica.configure(text=e, bg="red", fg="black", width=int(self.i*33), font=('times', int(self.i*15), 'bold'))
            self.Notifica.place(x=20*self.i, y=250*self.i)


    # ============Placing Button============
        # ============Placing Button============
    def register(self):
        def okay():

            username = self.register_username_entry.get()
            Id = self.register_username_entry.get()
            pwd = self.register_password_entry.get()
            register_win.destroy()

            select = "SELECT password FROM Student WHERE student_id={}".format(Id)
            cursor.execute(select)
            result = cursor.fetchall()

            if result == []:
                 #e = 'The current user is not in database, please input correct student ID'
                 #self.Notifica.configure(text=e, bg="red", fg="black", width=50, font=('times', 15, 'bold'))
                 #self.Notifica.place(x=20, y=450)
                 failure("register, \nThe current user is not in database ", "")
            elif str(pwd) != str(result[0][0]):
                 #e = 'The password is not correct, please input correct password'
                 #self.Notifica.configure(text=e, bg="red", fg="black", width=50, font=('times', 15, 'bold'))
                 #self.Notifica.place(x=20, y=450)
                 failure("register","")
            else:
                 #e = 'Training the model, please wait patiently'
                 #self.Notifica.configure(text=e, bg="green", fg="black", width=50, font=('times', 15, 'bold'))
                 #self.Notifica.place(x=20, y=450)
                 #self.window.mainloop(1)
                 register_win.destroy()
                 faceCapture(username)
                 #success("capture, \n please patiently wait for training", "")
                 train()

                 success("register!!!", self.window)

        register_win = Toplevel(self.window)
        register_win.title('Register for face regcognition system')
        register_win.geometry("1000x600+800+800")
        register_win.resizable(False, False)

        img = Image.open("images\\changebg.png")
        img = img.resize((int(1001*self.i), int(601*self.i)), Image.ANTIALIAS)
        self.changebg = ImageTk.PhotoImage(img)

        self.bg = Label(register_win, image=self.changebg)
        self.bg.pack(fill='both', expand='yes')
        self.username_label = Label(register_win, text="Username", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", int(self.i*13), "bold"))
        self.username_label.place(x=50*self.i, y=80*self.i)
        self.register_username_entry = Entry(register_win, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                             font=("yu gothic ui semibold", int(self.i*12)))
        self.register_username_entry.place(x=420*self.i, y=80*self.i, width=500*self.i)
        self.username_label = Label(register_win, text="password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", int(self.i*13), "bold"))
        self.username_label.place(x=50*self.i, y=220*self.i)
        self.register_password_entry = Entry(register_win, relief=FLAT, bg="alice blue", fg="#6b6a69",
                                             font=("yu gothic ui semibold", int(self.i*12)))
        self.register_password_entry.place(x=420*self.i, y=220*self.i, width=500*self.i)

        img = Image.open("images\\confirm.png")
        img = img.resize((int(401*self.i), int(122*self.i)), Image.ANTIALIAS)
        self.confirmNew = ImageTk.PhotoImage(img)

        self.confirml = Button(register_win, image=self.confirmNew, command=okay)
        self.confirml.place(x=300*self.i, y=400*self.i)

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
