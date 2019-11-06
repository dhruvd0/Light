
# test for pull request


from tkinter import Frame, Label, Entry, PhotoImage, Canvas, Tk, Button, Scrollbar, Checkbutton, IntVar
import os
import notifs
import webbrowser
import requests
import urllib
import web
import threading
from getpass import getpass
from bs4 import BeautifulSoup
import numpy as np
import threading


# UI---------------------
def search(query, string):
    for i in string.split():
        check1 = i.lower()
        check2 = query.lower()
        if check1 == check2:
            return True
    return False


def searchInString(query, string):
    for i in query.split():
        if (search(i, string) == False):
            return False
    return True


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
        self.events = []  # contains dicts of events
        self.powerImage = PhotoImage(file='Images/power.png')
        self.loginbg = PhotoImage(file='Images/loginbg2_image.png')
        self.mainbg = PhotoImage(file='Images/mainbg_image.png')
        self.loginimage = PhotoImage(file='Images/button_login.png')
        self.leftimage = PhotoImage(file='Images/left_image.png')
        self.rightimage = PhotoImage(file='Images/right_image.png')
        self.enterimage = PhotoImage(file='Images/enter_arrow.png')
        self.cancelimage = PhotoImage(file='Images/button_cancel.png')
        self.logoimage = PhotoImage(file='Images/logo4.png')
        try:

            temp = np.load("msg.npy", allow_pickle=True).item()
            self.unreads = list(temp)
        except FileNotFoundError:
            self.unreads = []
        except ValueError:
            self.unreads = []

        self.timeTable = []
        index = 0
        
        msgThread = threading.Thread(target=self.seeLastMessages).start()
        for i in os.listdir("Time_Table"):
            t = {}
            t["name"] = i
            t["image"] = PhotoImage(file="Time_Table/"+i)
            t["index"] = index
            index += 1
            self.timeTable.append(t)

        self.frames = {}

        self.autoLogin()

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
            try:
                if (self.frames[loginUI].c.get() == 1):

                    np.save("loginDetails.npy", self.d)
            except KeyError:
                pass

            self.show_frame(dashBoardUI)
            print("Hi ", self.userName)
            return True
        except AttributeError:
            #print (self.d)
            print("Invalid login please try again")
            self.frames[loginUI].label_error.place(
                relx=0.16, rely=0.75, relheight=0.06, relwidth=0.7)
            return False

    def autoLogin(self):  # checks if file has login data and launches gui if file is empty

        try:

            read_d = np.load('loginDetails.npy', allow_pickle=True).item()
            os.path.getsize('loginDetails.npy')
            self.userId = read_d["username"]
            self.userPass = read_d["password"]
            print("try block")
            try:

                test = requests.get(
                    "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1")
                self.loginLms()
            except requests.RequestException:

                print ("lms not working")
        except os.error:
            print("in os error")
            try:

                test = requests.get(
                    "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1")
                self.show_frame(loginUI)
            except requests.RequestException:

                print ("lms not working ")

    def seeLastMessages(self):
        while True:
            try:
              

                unreadCount = self.dashboardPage.find(
                    "label", {"class": "unreadnumber"}).text
                notifs.notify("You have " + unreadCount + " messages")
                break
               
            except TypeError:
                pass

    def fileSearch(self, searchName):  # returns a dictionary of file details
        try:
            courseHeadings = self.dashboardPage.find_all(
                "h4", {"class": "media-heading"})
            fileId = 0
            files = []  # dictionary of files returned
            courseHeadings = courseHeadings[0:int(len(courseHeadings)/2)]
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
                    if searchInString(searchName, resourceName):
                        fileId += 1
                        fileDict = {"id": fileId, "name": resourceName,
                                    "course": courseName, "url": resource.a["href"]}
                        files.append(fileDict)
                        
            if (len(files) == 0):
                return (False)
            else:
                self.files = files
                return (self.files)
        except AttributeError:
            pass

    def downloadFile(self, file):
        print ("DOWNLAODING :",file["name"])
        fileRequest = self.request_session.get(file["url"], stream=True)

        newFile = file["course"].replace(":", "_")
        file["course"] = newFile

        temp = file["name"].replace(" ", "_")
        file["name"] = temp
        print (fileRequest.headers["content-type"])
        '''if fileRequest.headers["content-type"] == "application/pdf":

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
            assignmentFileReq = self.request_session.get(
                assignmentDiv.a["href"])
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

            print ("not downloadable")'''

    
    def deadLines(self):
        try:
            read_d = np.load('events.npy')
            os.path.getsize("events.npy")
            print(read_d)
           
        except os.error:
            
            count = 0
            while(True):
                count += 1
                
                try:
                    calLink = self.dashboardPage.find(
                        "a", {"title": "This month"}).attrs["href"]
                    calendarRequest = self.request_session.get(calLink)
                    calendarPage = BeautifulSoup(
                        calendarRequest.content, "html5lib")  # main calendar page

                    liElements = calendarPage.find_all(
                        "li", {"class": "calendar_event_course"})  # li element
                    for liElement in liElements:
                        dayViewRequest = self.request_session.get(
                            liElement.a["href"])
                        dayViewPage = BeautifulSoup(
                            dayViewRequest.content, "html5lib")
                        h3Element = dayViewPage.find(
                            "h3", {"class": "referer"}, text=liElement.a.text)
                        event = {"name": h3Element.a.text,
                                 "link": h3Element.a["href"]}
                        fileReq = self.request_session.get(event["link"])
                        filePage = BeautifulSoup(fileReq.content, "html5lib")
                        if filePage.find("h3").text == "Submission status":
                            event["isSubmit"] = True
                        else:
                            event["isSubmit"] = False
                        self.events.append(event)
                        print("Saving event:", event)
                    np.save("events.npy", self.events)
                    return (True)
                except AttributeError:
                    pass
                except TypeError:
                    pass


class dashBoardUI(Frame):
    def __init__(self, parent, controller):
        self.day = 0
        controller.update()
        Frame.__init__(self, parent)
        self.controller = controller

        HEIGHT = 1080
        WIDTH = 1920

        canvas = Canvas(self, height=HEIGHT, width=WIDTH, bg='black')
        canvas.pack()

        mainlabel = Label(self, image=controller.mainbg)
        mainlabel.place(relheight=1, relwidth=1)

        frame = Frame(self, bg='black')
        frame.place(relx=0.8, relwidth=0.2, relheight=0.04)

        self.frame_display = Frame(self, bg='white')
        self.frame_display.place(relx=0.24, rely=0.23, relwidth=0.5, relheight=0.6)

        frame_dline = Frame(self, bg='white')
        frame_dline.place(relx=0.8, rely=0.23, relwidth=0.2, relheight=0.6)

        frame_tt = Frame(self, bg='white')
        frame_tt.place(rely=0.23, relwidth=0.2, relheight=0.6)

        frame_image = Frame(self, bg='white')
        frame_image.place(relx=0.40, rely=0.01, relwidth=0.15, relheight=0.1935)

        label_logo = Label(frame_image, image=controller.logoimage)
        label_logo.place(relheight=1, relwidth=1)

        label1 = Label(frame, text="WELCOME, " +
                       controller.userName, bg = 'black', fg = 'white', font=25)
        label1.pack()
        

        # labels for calender --------->
        self.label_tt_text = Label(
            frame_tt, text=controller.timeTable[self.day]["name"], font=30, bg='grey', fg='white')
        self.label_tt_text.place(relx=0.15, relheight=0.1, relwidth=0.7)

        self.label_tt1 = Label(
            frame_tt, bg='black', image=self.controller.timeTable[self.day]["image"])
        self.label_tt1.place(rely=0.1, relheight=0.9, relwidth=1)

        label_dline_text = Label(
            frame_dline, text="DEADLINES", bg='grey', fg='white', font=30)
        label_dline_text.place(relheight=0.1, relwidth=1)

        label_dline = Label(frame_dline, bg='black', fg='white', font=30)
        label_dline.place(rely=0.1, relheight=1, relwidth=1)

        label_main = Label(self.frame_display, bg='grey')
        label_main.place(relwidth=1, relheight=0.95)

        label_welcome = Label(self.frame_display, text = "TELL ME WHAT TO DO ....", bg = 'grey', fg = 'white', font = 10 )
        label_welcome.pack()

        button_main = Button(self.frame_display, text="-->", bg='white', fg='white', bd=0, image=controller.enterimage, command=lambda:self.searchThread(entry_main.get()) )
        button_main.place(rely=0.94, relx=0.9, relwidth=0.1, relheight=0.06)

        # buttons for time table ------->

        button_tt1 = Button(frame_tt, text='<-- ', bg='grey', fg='white',
                            activebackground='white', activeforeground='white', bd=0, image=controller.leftimage, command=self.dayLeft)
        button_tt1.place(relheight=0.1, relwidth=0.15)

        button_tt2 = Button(frame_tt, text='  -->', bg='grey', fg='white',
                            activebackground='white', activeforeground='white', bd=0, image=controller.rightimage, command=self.dayRight)
        button_tt2.place(relx=0.85, relheight=0.1, relwidth=0.15)

        button_exit = Button(self, text="EXIT", bg='black', fg='white',
                             activebackground='black', activeforeground='white', bd=0, command=controller.exitApp, image=controller.powerImage)
        button_exit.place(relx=0.93, rely=0.9, relheight=0.12, relwidth=0.06)
        # scrollbar for main window ------>

        scroll1 = Scrollbar(label_main, bg='black')
        scroll1.place(relheight=1, relx=0.98)

        entry_main = Entry(self.frame_display, bg='#393737', fg='white')
        entry_main.place(rely=0.94, relwidth=0.9, relheight=0.06)

    def dayLeft(self):
        if self.day == 0:
            self.day = 4

        else:
            self.day = self.day-1
        self.label_tt1.config(
            image=self.controller.timeTable[self.day]["image"])
        self.label_tt_text.config(
            text=self.controller.timeTable[self.day]["name"])

    def dayRight(self):
        if self.day == 4:
            self.day = 0

        else:
            self.day = self.day+1
        self.label_tt1.config(
            image=self.controller.timeTable[self.day]["image"])
        self.label_tt_text.config(
            text=self.controller.timeTable[self.day]["name"])

    def searchThread(self,name):
        t=threading.Thread(target=self.mainSearch,args=(name,))
        t.start()
    def mainSearch(self, query):

        self.searchResult=self.controller.fileSearch(query)
        if(self.searchResult == False):

            web.openWeb(query)
        else:
            #print (self.searchResult)
            self.mainwindow()

    def mainwindow(self):
        
        a = 0.1 #relx
        b = 0.2 #rely
        frame_wait = Frame(self.frame_display)
        frame_wait.place(relx = 0.32,rely = 0.12)

        label_wait = Label(frame_wait, text = "Here are the following results ....", bg = 'grey', fg = 'white',font = 10)
        label_wait.pack()
        for currFile in self.controller.files:
            frame_label = Frame(self.frame_display)
            frame_label.place(relx = a, rely = b)
            label_name = Label(frame_label,text = currFile["course"], bg = 'grey', fg = 'white', font = 15)
            label_name.pack()
            
            frame_inside = Frame(self.frame_display, bg = 'white')
            frame_inside.place(relx = 0.7,rely = b)
            button = Button(frame_inside,text = currFile["name"], bg = 'grey', fg = 'white', bd = 1,command=lambda:print(currFile))
            button.pack()
            
            
            b= b+0.1

            



class loginUI(Frame):
    def __init__(self, parent, controller):

        self.controller = controller
        Frame.__init__(self, parent, bg="black",)
        height = 500
        width = 550
        canvas = Canvas(
            self, height=height, width=width, bg='black')
        canvas.pack()

        loginlabel = Label(self, image=controller.loginbg)
        loginlabel.place(relheight=1, relwidth=1)

        b = Button(self, text="Submit", bg='#202021', fg='white', activebackground='black',
                   activeforeground='white', bd=0, image=controller.loginimage, command=lambda: self.getDat())
        b.place(relx=0.22, rely=0.68, relheight=0.05, relwidth=0.315)

        b2 = Button(self, text="Cancel", bg='#202021', fg='white', activebackground='black',
                    bd=0, activeforeground='white', image=controller.cancelimage)
        b2.place(relx=0.6, rely=0.68, relheight=0.05, relwidth=0.317)

        # --------------------------------------
        self.c = IntVar()
        self.check = Checkbutton(self, text='Remember ID and Password', bg='#202021',
                                 fg='grey', activeforeground='white', activebackground='#202021', variable=self.c)
        self.check.place(relx=0.4, rely=0.59)

        self.label_logo = Label(
            self, text="LIGHT", fg='white', font=1000, bg='#202021', image=controller.logoimage)
        self.label_logo.place(relx=0.35, relheight=0.33, relwidth=0.4)
        self.label2 = Label(
            self, text="Password: ", bg='#38383A', fg='white', font=23)
        self.label2.place(relx=0.15, rely=0.48)

        self.label1 = Label(
            self, text="Username: ", bg='#38383A', fg='white', font=23)
        self.label1.place(relx=0.15, rely=0.38)

        self.label_error = Label(self, text='''You have entered your password or username incorrectly. 
        Please check and try again. ''', fg='white', bg='#38383A', bd=2)

        self.entry_user = Entry(self, bg='#202021', fg='white', bd=2)
        self.entry_user.place(relx=0.4, rely=0.38,
                              relheight=0.05, relwidth=0.5)
        self.entry_pass = Entry(
            self, bg='#202021', fg='white', show="*", bd=2)
        self.entry_pass.place(relx=0.4, rely=0.48,
                              relheight=0.05, relwidth=0.5)

        # --------------------------------------------

    def getDat(self):

        self.controller.userId = self.entry_user.get()
        self.controller.userPass = self.entry_pass.get()

        self.controller.loginLms()

# -------------------------------------------------------------


app = App()


app.mainloop()



np.save("msg.npy", app.unreads)
