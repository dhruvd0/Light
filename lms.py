
# Use this file to test and learn requests and Beautiful soup
import notifs
import webbrowser
import requests
import urllib
from getpass import getpass
from bs4 import BeautifulSoup

d={}
request_session=requests.Session()
def loginLms():
    userId = input("enter user:")  # user id eg:e19cse001
    userPass = getpass("enter pass:")
    d = {"username": userId, "password": userPass}  # form data to be submitted
    userName = ""
   
    login = request_session.post(
        "http://lms.bennett.edu.in/login/index.php?authldap_skipntlmsso=1", data=d)  # post request
    # soup element which has all the html content
    soup = BeautifulSoup(login.content, "html5lib")
    
    try:
        userName = soup.find("span", {"class": "usertext"}).text
        notifs.loginSuccess(userName)  # windows toast notification
        print("Hi ", userName)
        return soup
    except AttributeError:
        print("Invalid Login Please try agin")
        loginLms()


loginLms()

