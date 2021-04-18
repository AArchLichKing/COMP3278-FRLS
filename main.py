from tkinter import *
import tkinter as tk
from PIL import ImageTk
from homePage import home_win
import datetime, time
import random
import cv2
from faceCapture import faceCapture
from train import train
import mysql.connector
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
myconn = mysql.connector.connect(host="localhost", user="root", passwd="010207", database="db")
cursor = myconn.cursor()

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

        self.submit = ImageTk.PhotoImage \
            (file='images\\login.png')

        self.submit_button = Button(self.window, command = self.manuallySignIn, image=self.submit, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.submit_button.place(x=1800, y=940)

        self.face= ImageTk.PhotoImage \
            (file='images\\face.png')
        self.face_button = Button(self.window, command=self.autoSignIn, image=self.face, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.face_button.place(x=2660, y=940)
        
        self.Notifica = tk.Label(self.window, text="", bg="Green", fg="white", width=33,
                            height=2, font=('times', 15, 'bold'))

        # ============Placing Button============
        self.register_img = ImageTk.PhotoImage \
            (file='images\\Register.png')

        self.login_button = Button(self.window, command=self.register, image=self.register_img, relief=FLAT, borderwidth=0, background="white",
                                    activebackground="white", cursor="hand2")
        self.login_button.place(x=1800, y=500)

    def autoSignIn(self):
        now = time.time()  ###For calculate seconds of video
        future = now + 20
        login_flag = 0
        best_conf = 70
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
                recognizer.read("TrainingImageLabel\Trainer_1.yml")
            except:
                e = 'Model not found or corrupted,Please train the model by clicking Register New Student'
                self.Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                self.Notifica.place(x=20, y=250)

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
                        
                    if (conf <70):
                        #Is registered student
                        print(conf)
                        ts = time.time()
                        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                        global tt
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)                        
                        #open main page according to Id, close login page
                        login_flag += 1
                    else:
                        Id = 'Unknown'
                        tt = str(Id)
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                if time.time() > future:
                    break
                
                cv2.imshow('Checking Identity..', im)
                key = cv2.waitKey(30) & 0xff
                if key == 27 or login_flag > 10:
                    break
                    
            cam.release()
            cv2.destroyAllWindows()
            
            if  login_flag > 10:
                Id = 1 # for testing purpose
                self.window.destroy()
                home_win(Id)

    def manuallySignIn(self):
        #record sign in time
        global ts
        global date
        global timeStamp
        
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        
        #read username from blank
        Id = self.username_entry.get()
        
        #get pwd
        select = "SELECT password FROM Student WHERE student_id='%s'" % (Id)
        name = cursor.execute(select)
        result = cursor.fetchall() 
                   
        #compare with corresponding pwd            
        match = result[0][0] == self.password_entry.get()            
        if match:
            #open main page according to Id, close login page
            self.window.destroy()
            home_win(Id)
        else:
            #generate err message
            e = 'You are not legal student! Please input right username' if result==[] else 'Wrong pwd!'
            self.Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
            self.Notifica.place(x=20, y=250)

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
                e = 'The current user is not in database, please input correct student ID'
                reg_Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                reg_Notifica.place(x=20, y=250)
            elif str(pwd) != str(result[0][0]):
                e = 'The password is not correct, please input correct password'
                reg_Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                reg_Notifica.place(x=20, y=250)
            else:  
                #username is in the database and pwd correct
                register_win.destroy()
                faceCapture(username)

                if True:
                    #train new model with data
                    print('Start Training')
                    train()
            
            
        #read username from blank
        register_win = Toplevel(self.window)
        register_win.title('Register for face regcognition system')
        register_win.geometry("1000x600+800+800")
        register_win.resizable(False, False)
        self.changebg = ImageTk.PhotoImage \
            (file='images\\changebg.png')
        self.bg = Label(register_win, image=self.changebg)
        self.bg.pack(fill='both', expand='yes')
        self.username_label = Label(register_win, text="Username", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=50, y=80)
        self.register_username_entry = Entry(register_win, relief=FLAT, bg="alice blue", fg="#6b6a69", 
                                    font=("yu gothic ui semibold", 12))
        self.register_username_entry.place(x=420, y=80, width=500)
        self.username_label = Label(register_win, text="password", bg="white", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=50, y=220)
        self.register_password_entry = Entry(register_win, relief=FLAT, bg="alice blue", fg="#6b6a69", 
                                    font=("yu gothic ui semibold", 12))
        self.register_password_entry.place(x=420, y=220, width=500)

        self.confirmNew = ImageTk.PhotoImage \
            (file='images\\confirm.png')
        self.confirml = Button(register_win, image=self.confirmNew, command=okay)
        self.confirml.place(x=300, y=400)

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
