
# Use this file to test and learn requests and Beautiful soup

import tkinter as tk1
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
#import mainGui

# Globals
d = {}
request_session = requests.Session()

userId = "id "
userPass = " pass"
userName = "user"
dashboardPage = "dash"


def autoLogin(self):  # checks if file has login data and launches gui if file is empty
    global userPass
    global userId
    try:

        read_d = np.load('my_file.npy').item()
        os.path.getsize('my_file.npy')
        userId = read_d["username"]
        userPass = read_d["password"]
        print("try block")
        loginLms()

    except os.error:
        


def loginLms():  # sends a request to website for login => pushes a toast notif if successfull

    d = {"username": userId, "password": userPass}
    global dashboardPage
    login = request_session.post(
        "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1", data=d)  # post request
    # soup element which has all the html content
    dashboardPage = BeautifulSoup(login.content, "html5lib")

    try:
        userName = dashboardPage.find("span", {"class": "usertext"}).text
        app.exit()
        notifs.loginSuccess(userName)  # windows toast notification
        
        np.save("my_file.npy", d)
        #mainGui.root.mainloop()
        print("Hi ", userName)

    except AttributeError:
        print("Invalid Login Please try agin")
        app.button.config(text="Invalid Login Please try agin")
        
        app.root.update()
        


def seeLastMessages():
    unreadCount = dashboardPage.find("label", {"class": "unreadnumber"}).text
    print("You have ", unreadCount, " messages:")

    messagesRequest = request_session.get(
        "http://lms.bennett.edu.in/message/index.php")
    messagePage = BeautifulSoup(messagesRequest.content, "html5lib")
    messages = messagePage.find_all("span", {"class": "text"})
    for message in messages:
        print(message.text)


def fileSearch(searchName):  # returns a dictionary of file details
    # input("File to search:")
    courseHeadings = dashboardPage.find_all("h4", {"class": "media-heading"})
    fileId = 0
    files = []  # dictionary of files returned

    for courseHead in courseHeadings:

        courseLink = courseHead.a["href"]

        courseRequest = request_session.get(courseLink)
        coursePage = BeautifulSoup(courseRequest.content, "html5lib")
        resources = coursePage.find_all("div", {"class": "activityinstance"})

        courseName = "".join([i for i in courseHead.text.split() if i != " "])

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
                return (i)


def downloadFile(file):
    #print (file["url"])
    fileRequest = request_session.get(file["url"], stream=True)

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
        assignmentPageRequest = request_session.get(file["url"])
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
        linkReq = request_session.get(file["url"], stream=True)

        print(linkReq.headers["content-type"])


def deadLines():
    calLink = dashboardPage.find("a", {"title": "This month"}).attrs["href"]
    calendarRequest = request_session.get(calLink)
    calendarPage = BeautifulSoup(calendarRequest.content, "html5lib")
    events = []
    calendarEvents = calendarPage.find_all(
        "ul", {"class": "events-new"})  # ul element
    for calendarEvent in calendarEvents:
        eves = calendarEvent.find_all("li")
        event = {}
        for i in eves:
            event["name"] = eves.a.text
            events.append(event)
    return (events)


#print (deadLines())


loginThread=threading.Thread(target=autoLogin)
print ("hello")
print ("hello")
loginThread.start()

