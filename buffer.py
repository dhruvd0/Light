from tkinter import *
import os
import notifs
import webbrowser
import requests
import urllib
import web
from getpass import getpass
from bs4 import BeautifulSoup
import wget
import numpy as np
import threading

d = {}
request_session = requests.Session()

userId = "id "
userPass = " pass"
userName = "user"
dashboardPage = "dash"

# UI---------------------


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (loginUI, dashBoardUI):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        

        d = {}
        request_session = requests.Session()

        userId = "id "
        userPass = " pass"
        userName = "user"
        dashboardPage = "dash"

        self.show_frame(loginUI)

     
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()
    def loginLms(self):  # sends a request to website for login => pushes a toast notif if successfull

        self.d = {"username": self.userId, "password": self.userPass}

        login = self.request_session.post(
            "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1", data=self.d)  # post request
        # soup element which has all the html content
        self.dashboardPage = BeautifulSoup(login.content, "html5lib")

        try:
            self.userName = dashboardPage.find(
                "span", {"class": "usertext"}).text

            notifs.loginSuccess(self.userName)  # windows toast notification

            np.save("my_file.npy", d)
            # mainGui.root.mainloop()
            print("Hi ", self.userName)

        except AttributeError:
            print ("Invalid login please try again")
        

    def autoLogin(self):  # checks if file has login data and launches gui if file is empty
        
        try:

            read_d = np.load('my_file.npy').item()
            os.path.getsize('my_file.npy')
            self.userId = read_d["username"]
            self.userPass = read_d["password"]
            print("try block")
            self.loginLms()

        except os.error:
            print ("in os error")
            self.show_frame(loginUI)

  

    def exitApp(self):
        self.destroy()

        print("Invalid Login Please try agin")
        self.frames[loginUI].b.config(text="test")

        app.update()


class loginUI(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black",)
        height = 500
        width = 550
        canvas = Canvas(
            self, height=height, width=width, bg='black')
        canvas.pack()
        b = Button(self, text="Submit", bg='#1f1f14', fg='white', activebackground='black',
                   activeforeground='white', command=lambda: controller.show_frame(dashBoardUI))
        b.place(relx=0.5, rely=0.61, relheight=0.05, relwidth=0.2)

        # --------------------------------------

        label_logo = Label(
            self, text="LIGHT", fg='white', font=1000, bg='black')
        label_logo.place(relx=0.4, relheight=0.2, relwidth=0.2)
        label2 = Label(
            self, text="Password: ", bg='black', fg='white', font=25)
        label2.place(relx=0.15, rely=0.5,)

        label1 = Label(
            self, text="Username: ", bg='black', fg='white', font=25)
        label1.place(relx=0.15, rely=0.4)

        entry_user = Entry(self, bg='#1f1f14', fg='white')
        entry_user.place(relx=0.4, rely=0.41,
                         relheight=0.05, relwidth=0.5)
        entry_pass = Entry(
            self, bg='#1f1f14', fg='white', show="*")
        entry_pass.place(relx=0.4, rely=0.51,
                         relheight=0.05, relwidth=0.5)

        # --------------------------------------------


class dashBoardUI(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        HEIGHT = 1080
        WIDTH = 1920

        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg='black')
        canvas.pack()

        frame = Frame(self, bg='black')
        frame.place(relx=0.7, relwidth=0.3, relheight=0.20)

        frame_display = Frame(self, bg='white')
        frame_display.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.6)

        frame_dline = Frame(self, bg='white')
        frame_dline.place(relx=0.8, rely=0.2, relwidth=0.3, relheight=0.299)

        frame_cal = Frame(self, bg='white')
        frame_cal.place(relx=0.8, rely=0.5, relwidth=0.3, relheight=0.3)

        frame_tt = Frame(self, bg='white')
        frame_tt.place(rely=0.2, relwidth=0.2, relheight=0.6)

        frame_image = Frame(self, bg='white')
        frame_image.place(relx=0.37, rely=0.01, relwidth=0.2, relheight=0.1)

        frame_sugg = Frame(self, bg='black')
        frame_sugg.place(rely=0.85, relwidth=1, relheight=0.1)

        label1 = Label(frame, text="WELCOME, USER",
                       bg='black', fg='white', font=25)
        label1.pack()

        # labels for calender --------->
        label_tt1 = Label(frame_tt, text="Time table", font=20)
        label_tt1.place(rely=0.1, relheight=1, relwidth=1)

        label_dline = Label(frame_dline, text="DEADLINES", fg='black', font=30)
        label_dline.place(relheight=1, relwidth=1)

        label_cal1 = Label(frame_cal, text="CALENDER", font=15)
        label_cal1.place(relx=0.08, relheight=0.1, relwidth=0.5)

        label_cal2 = Label(frame_cal)
        label_cal2.place(rely=0.1, relheight=0.9, relwidth=1)

        label_sugg = Label(frame_sugg, text='Suggestions: ',
                           font=20, bg='black', fg='white')
        label_sugg.place(relwidth=0.14, relheight=0.3)

        label_main = Label(frame_display)
        label_main.place(relwidth=1, relheight=0.95)

        button_main = Button(frame_display, text="-->", bg='black', fg='white', activebackground='black',
                             activeforeground='white',)  # command=lambda: main_input(entry_main.get())
        button_main.place(rely=0.94, relx=0.9, relwidth=0.1, relheight=0.06)

        button_cal1 = Button(frame_cal, text="<--", bg='#1f1f14',
                             fg='white', activebackground='black', activeforeground='white')
        button_cal1.place(relx=0.0001, relheight=0.1, relwidth=0.1)

        button_cal1 = Button(frame_cal, text="-->", bg='#1f1f14',
                             fg='white', activebackground='black', activeforeground='white')
        button_cal1.place(relx=0.55, relheight=0.1, relwidth=0.1)

        # buttons for time table ------->

        button_tt1 = Button(frame_tt, text='<--', bg='#1f1f14', fg='white',
                            activebackground='black', activeforeground='white')
        button_tt1.place(relheight=0.1, relwidth=0.15)

        button_tt2 = Button(frame_tt, text='-->', bg='#1f1f14', fg='white',
                            activebackground='black', activeforeground='white')
        button_tt2.place(relx=0.85, relheight=0.1, relwidth=0.15)

        # suggestion buttons ------>

        button_sugg1 = Button(frame_sugg, text='Suggestion 1', bg='#1f1f14',
                              fg='white', activebackground='black', activeforeground='white')
        button_sugg1.place(relx=0.05, rely=0.45, relheight=0.4, relwidth=0.15)

        button_sugg2 = Button(frame_sugg, text='Suggestion 2', bg='#1f1f14',
                              fg='white', activebackground='black', activeforeground='white')
        button_sugg2.place(relx=0.25, rely=0.45, relheight=0.4, relwidth=0.15)

        button_sugg3 = Button(frame_sugg, text='Suggestion 3', bg='#1f1f14',
                              fg='white', activebackground='black', activeforeground='white')
        button_sugg3.place(relx=0.45, rely=0.45, relheight=0.4, relwidth=0.15)

        button_sugg4 = Button(frame_sugg, text='Suggestion 4', bg='#1f1f14',
                              fg='white', activebackground='black', activeforeground='white')
        button_sugg4.place(relx=0.65, rely=0.45, relheight=0.4, relwidth=0.15)

        button_exit = Button(frame_sugg, text="EXIT", bg='#1f1f14', fg='white',
                             activebackground='black', activeforeground='white', command=controller.exitApp)
        button_exit.place(relx=0.85, rely=0.25, relheight=0.4, relwidth=0.08)

        # scrollbar for main window ------>

        scroll1 = Scrollbar(label_main, bg='blue')
        scroll1.place(relheight=1, relx=0.98)

        entry_main = Entry(frame_display, bg='white', fg='black')
        entry_main.place(rely=0.94, relwidth=0.9, relheight=0.06)


# -------------------------------------------------------------


app = App()

