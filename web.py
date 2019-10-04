
# Use this file to test and learn requests and Beautiful soup
import notifs
import webbrowser
import requests
import urllib
from getpass import getpass
from bs4 import BeautifulSoup

def isValidInternet():
    try:
        r = requests.get("http://www.google.com")
        return True
    except requests.exceptions.ConnectionError:
        return False

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
