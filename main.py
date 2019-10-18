
# test for pull request


from tkinter import *
import os
import notifs
import webbrowser
import requests
import urllib
import web
from getpass import getpass
from bs4 import BeautifulSoup

import numpy as np
import threading


# UI---------------------


class App(Tk):
    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        self.d = {}
        self.request_session = requests.Session()
        self.userId = "id "
        self.userPass = " pass"
        self.userName = "name"
        self.dashboardPage = "dash"
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # use this to debug functions:

        self.autoLogin()
        print(self.deadLines())
        # self.exitApp()
        # --------
        # self.show_frame(loginUI)

    def show_frame(self, context):
        frame = context(self.container, self)
        self.frames[context] = frame
        frame.grid(row=0, column=0)
        frame.tkraise()

    def getName(self):
        print("test")

    def exitApp(self):
        print("test")
        self.destroy()

    def loginLms(self):  # sends a request to website for login => pushes a toast notif if successfull

        self.d = {"username": self.userId, "password": self.userPass}

        login = self.request_session.post(
            "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1", data=self.d)  # post request
        # soup element which has all the html content
        self.dashboardPage = BeautifulSoup(login.content, "html5lib")

        try:
            self.userName = self.dashboardPage.find(
                "span", {"class": "usertext"}).text
           # notifs.loginSuccess(self.userName)
            np.save("my_file.npy", self.d)

            print("Hi ", self.userName)

            # self.show_frame(dashBoardUI)

            notifs.loginSuccess(self.userName)  # windows toast notification

            return True

        except AttributeError:
            #print (self.d)
            print("Invalid login please try again")
            self.frames[loginUI].label_error.place(
                relx=0.16, rely=0.75, relheight=0.06, relwidth=0.7)

            return False

    def autoLogin(self):  # checks if file has login data and launches gui if file is empty

        try:

            read_d = np.load('my_file.npy').item()
            os.path.getsize('my_file.npy')
            self.userId = read_d["username"]
            self.userPass = read_d["password"]
            print("try block")
            self.loginLms()

        except os.error:

            self.show_frame(loginUI)

    def seeLastMessages(self):
        unreadCount = self.dashboardPage.find(
            "label", {"class": "unreadnumber"}).text
        print("You have ", unreadCount, " messages:")

        messagesRequest = request_session.get(
            "http://lms.bennett.edu.in/message/index.php")
        messagePage = BeautifulSoup(messagesRequest.content, "html5lib")
        messages = messagePage.find_all("span", {"class": "text"})
        for message in messages:
            print(message.text)

    def fileSearch(self, searchName):  # returns a dictionary of file details
        # input("File to search:")
        courseHeadings = self.dashboardPage.find_all(
            "h4", {"class": "media-heading"})
        fileId = 0
        files = []  # dictionary of files returned

        for courseHead in courseHeadings:

            courseLink = courseHead.a["href"]

            courseRequest = self.request_session.get(courseLink)
            coursePage = BeautifulSoup(courseRequest.content, "html5lib")
            resources = coursePage.find_all(
                "div", {"class": "activityinstance"})

            courseName = "".join(
                [i for i in courseHead.text.split() if i != " "])

            for resource in resources:

                resourceName = resource.span.text
                filterName = resourceName.split()
                resourceName = " ".join(
                    [i for i in filterName if i != "File" and i != "URL"])

                if resourceName == searchName:
                    fileId += 1

                    fileDict = {"id": fileId, "name": resourceName,
                                "course": courseName, "url": resource.a["href"]}
                    files.append(fileDict)
                    break
        if (len(files) == 0):
            return ("No files Found")
        else:
            for i in files:
                print(i, "\n")
            id = 1  # int(input("Select fle id:"))
            for i in files:

                if(i["id"] == id):
                    self.file = i

    def downloadFile(self, file):
        #print (file["url"])
        fileRequest = self.request_session.get(file["url"], stream=True)

        newFile = file["course"].replace(":", "_")
        file["course"] = newFile

        temp = file["name"].replace(" ", "_")
        file["name"] = temp
        if fileRequest.headers["content-type"] == "application/pdf":

            path = file["course"]+"/"+file["name"]+".pdf"
            try:
                with open(path, 'wb') as f:
                    f.write(fileRequest.content)
            except OSError:
                os.mkdir(file["course"])
                with open(path, 'wb') as f:
                    f.write(fileRequest.content)
        # Submittable Assignment File
        elif BeautifulSoup(fileRequest.content, "html5lib").find("head").title.text == "Assignment":
            assignmentPageRequest = self.request_session.get(file["url"])
            assignmentPage = BeautifulSoup(
                assignmentPageRequest.content, "html5lib")
            assignmentDiv = assignmentPage.find("div", {"id": "intro"})
            file["name"] = assignmentDiv.a.text
            assignmentFileReq = request_session.get(assignmentDiv.a["href"])
            path = file["course"]+"/"+file["name"]
            try:
                with open(path, 'wb') as t:
                    t.write(assignmentFileReq.content)
            except OSError:
                os.mkdir(file["course"])
                with open(path, 'wb') as t:
                    t.write(assignmentFileReq.content)
        else:
            linkReq = self.request_session.get(file["url"], stream=True)

            print(linkReq.headers["content-type"])

    def deadLines(self):
        calLink = self.dashboardPage.find(
            "a", {"title": "This month"}).attrs["href"]
        calendarRequest = self.request_session.get(calLink)
        calendarPage = BeautifulSoup(
            calendarRequest.content, "html5lib")  # main calendar page
        events = []  # contains dicts of events
        liElements = calendarPage.find_all(
            "li", {"class": "calendar_event_course"})  # li element

        #print(liElements)

        for liElement in liElements:
            dayViewRequest = self.request_session.get(liElement.a["href"])
            dayViewPage = BeautifulSoup(dayViewRequest.content, "html5lib")
            h3Element = dayViewPage.find(
                "h3", {"class": "referer"}, text=liElement.a.text)
            event = {"name": h3Element.a.text, "link": h3Element.a["href"]}

            fileReq = self.request_session.get(event["link"])
            filePage = BeautifulSoup(fileReq.content, "html5lib")
            if filePage.find("h3").text == "Submission status":
                event["isSubmit"] = True
                
            else:
                event["isSubmit"] = False

            events.append(event)[]

        for i in events:
            print(i)

        


class dashBoardUI(Frame):
    def __init__(self, parent, controller):

        controller.update()
        Frame.__init__(self, parent)
        self.controller = controller

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

        label1 = Label(frame, text="WELCOME, "+controller.userName,
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
                             activeforeground='white')  # command=lambda: main_input(entry_main.get())
        button_main.place(rely=0.94, relx=0.9, relwidth=0.1, relheight=0.06)

        button_cal1 = Button(frame_cal, text="<--", bg='#1f1f14',
                             fg='white', activebackground='black', activeforeground='white')
        button_cal1.place(relx=0.0001, relheight=0.1, relwidth=0.1)

        button_cal1 = Button(frame_cal, text="-->", bg='#1f1f14',
                             fg='white', activebackground='black', activeforeground='white')
        button_cal1.place(relx=0.55, relheight=0.1, relwidth=0.1)

        # buttons for time table ------->

        button_tt1 = Button(frame_tt, text='<-- ', bg='#1f1f14', fg='white',
                            activebackground='black', activeforeground='white')
        button_tt1.place(relheight=0.1, relwidth=0.15)

        button_tt2 = Button(frame_tt, text='  -->', bg='#1f1f14', fg='white',
                            activebackground='black', activeforeground='white')
        button_tt2.place(relx=0.85, relheight=0.1, relwidth=0.15)

        # suggestion buttons ------>
        button_openfile = PhotoImage(file='Images/button_open-file.png')
        button_sugg1 = Button(frame_sugg, text='Suggestion 1', bg='black',
                              fg='white', activebackground='black', activeforeground='white', bd=0, image=button_openfile)
        button_sugg1.place(relx=0.05, rely=0.45, relheight=0.45, relwidth=0.13)

        button_search = PhotoImage(file='Images/button_search.png')
        button_sugg2 = Button(frame_sugg, text='Suggestion 2', bg='black',
                              fg='white', activebackground='black', activeforeground='white', bd=0, image=button_search)
        button_sugg2.place(relx=0.25, rely=0.45, relheight=0.45, relwidth=0.12)

        button_sugg3 = Button(frame_sugg, text='Suggestion 3', bg='black',
                              fg='white', activebackground='black', activeforeground='white', bd=0)
        button_sugg3.place(relx=0.45, rely=0.45, relheight=0.4, relwidth=0.15)
        button_messages = PhotoImage(file='Images/button_show-messages.png')
        button_sugg4 = Button(frame_sugg, text='Suggestion 4', bg='black',
                              fg='white', activebackground='black', activeforeground='white', bd=0, image=button_messages)
        button_sugg4.place(relx=0.65, rely=0.45, relheight=0.4, relwidth=0.15)

        button_power = PhotoImage(file='Images/power1.png')
        button_exit = Button(frame_sugg, text="EXIT", bg='#1f1f14', fg='white',
                             activebackground='black', activeforeground='white', bd=0, command=controller.exitApp,)
        button_exit.place(relx=0.85, rely=0.45, relheight=0.8, relwidth=0.08)
        # scrollbar for main window ------>

        scroll1 = Scrollbar(label_main, bg='blue')
        scroll1.place(relheight=1, relx=0.98)

        entry_main = Entry(frame_display, bg='white', fg='black')
        entry_main.place(rely=0.94, relwidth=0.9, relheight=0.06)

    def exitUI(self):
        print("test")


class loginUI(Frame):
    def __init__(self, parent, controller):

        self.controller = controller
        Frame.__init__(self, parent, bg="black",)
        height = 500
        width = 550
        canvas = Canvas(
            self, height=height, width=width, bg='black')
        canvas.pack()
        b = Button(self, text="Submit", bg='#1f1f14', fg='white', activebackground='black',
                   activeforeground='white', command=lambda: self.getDat())
        b.place(relx=0.5, rely=0.61, relheight=0.05, relwidth=0.2)

        # --------------------------------------
        self.label_logo = Label(
            self, text="LIGHT", fg='white', font=1000, bg='#0a0a0a')
        self.label_logo.place(relx=0.4, relheight=0.2, relwidth=0.2)
        self.label2 = Label(
            self, text="Password: ", bg='#0a0a0a', fg='white', font=23)
        self.label2.place(relx=0.15, rely=0.5)

        self.label1 = Label(
            self, text="Username: ", bg='#0a0a0a', fg='white', font=23)
        self.label1.place(relx=0.15, rely=0.4)

        self.label_error = Label(self, text='''You have entered your password or username incorrectly. 
        Please check and try again. ''', fg='red', bg='white', bd=0)

        self.entry_user = Entry(self, bg='#1f1f14', fg='white')
        self.entry_user.place(relx=0.4, rely=0.41,
                              relheight=0.05, relwidth=0.5)
        self.entry_pass = Entry(
            self, bg='#1f1f14', fg='white', show="*")
        self.entry_pass.place(relx=0.4, rely=0.51,
                              relheight=0.05, relwidth=0.5)

        # --------------------------------------------
    def getDat(self):

        self.controller.userId = self.entry_user.get()
        self.controller.userPass = self.entry_pass.get()

        self.controller.loginLms()


class testFrame(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        HEIGHT = 1080
        WIDTH = 1920

        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg='white')
        canvas.pack()


# -------------------------------------------------------------

app = App()
app.mainloop()
