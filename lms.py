
# Use this file to test and learn requests and Beautiful soup
import os
import notifs
import webbrowser
import requests
import urllib
from getpass import getpass
from bs4 import BeautifulSoup
import wget
d = {}
request_session = requests.Session()


def loginLms():

    userId = input("enter user:")  # user id eg:e19cse001
    userPass = getpass("enter pass:")
    # form data to be submitted
    d = {"username": userId, "password": userPass}
    userName = ""

    login = request_session.post(
        "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1", data=d)  # post request
    # soup element which has all the html content
    dashboardPage = BeautifulSoup(login.content, "html5lib")

    try:
        userName = dashboardPage.find("span", {"class": "usertext"}).text
        notifs.loginSuccess(userName)  # windows toast notification
        print("Hi ", userName)
        return dashboardPage
    except AttributeError:
        print("Invalid Login Please try agin")
        loginLms()


def seeLastMessages():
    unreadCount = dashboardPage.find("label", {"class": "unreadnumber"}).text
    print("You have ", unreadCount, " messages:")

    messagesRequest = request_session.get(
        "http://lms.bennett.edu.in/message/index.php")
    messagePage = BeautifulSoup(messagesRequest.content, "html5lib")
    messages = messagePage.find_all("span", {"class": "text"})
    for message in messages:
        print(message)


def fileSearch():
    searchName = "Tutorial 1"  # input("File to search:")
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
    for i in files:
        print(i, "\n")
    id = int(input("Select fle id:"))
    for i in files:
        if(i["id"] == id):
            return (i)


def downloadFile(file):
    fileRequest = request_session.get(file["url"], stream=True)

    if fileRequest.headers["content-type"] == "application/pdf":
        path = file["name"]+".pdf"
        with open(path, 'wb') as f:
            f.write(fileRequest.content)


dashboardPage = loginLms()
downloadFile(fileSearch())
