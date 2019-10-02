
# Use this file to test and learn requests and Beautiful soup

import webbrowser
import requests
import urllib
from getpass import getpass
from bs4 import BeautifulSoup


def checkDictionary():
    pass


def getWeather():
    return ("shows weather")


def isValidInternet():
    try:
        r = requests.get("http://www.google.com")
        return True
    except requests.exceptions.ConnectionError:
        return False


def loginLms():
    os.system("cls")
    #gets user details
    userId = input("enter user:")
    userPass = getpass("enter pass:")

    d = {"username": userId, "password": userPass}

    login = requests.post(
        "http://lms.bennett.edu.in/login/index.php", data=d)  # post request
    soup = BeautifulSoup(login.content, "html5lib")
    userName = soup.find("span", {"class": "usertext"}).text

    courses = soup.find_all("h4", {"class": "media-heading"})
    print("Hi ", userName)
    print("Your courses:")
    for courseName in courses:
        print(courseName.text)



def openWeb(link):  # checks if the links is valid
    mainLink = link
    if (link[0:12] != "http://www."):
        temp = "http://www."
        temp = temp+link
        link = temp
    try:
        request = requests.get(link)

    except requests.exceptions.MissingSchema:
        link = "https://www.google.com/search?q="+mainLink

    except requests.exceptions.ConnectionError:
        link = "https://www.google.com/search?q="+mainLink
    webbrowser.open(link)
