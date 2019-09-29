import os  # os.system(string) is used to run cmd commands
import urllib
import re
import user
#import requests
import json
from datetime import datetime
#import tkinter as tk
#import kivy
#from kivy.app import App
#from kivy.uix.label import Label
import web
def checkIn(userIn):  # checks if user input is alphanumeric
    for x in userIn:
        if x.isalpha() == False:
            print("string is not valid")
    else:
        print("                                  Sure i can do that")



def getDatetime():
    n = datetime.now()
    dt = str(n.date()) + str(n.time())  # combination of date and timewha
    return (dt)


def openApps():
    pass


def showSchedule():
    pass



def thankYou():
    print("\n Thank you \n")
    print("\n Version : 1.0.0 ")
    print("Support : https://github.com/dhruvd0/End-Sem-Project \n")
    print ("")

def Main():  # main display and user input
    print("                                                            WELCOME \n \n")
    userIn = input(
        "                            Ask me Anything \n                                                        ~ ")

    exit_op = ["quit", "bye", "ttly", "exit", ]  # types of saying bye/quit

    while(True):
        if userIn in exit_op:
            break

        response = "\n                            " + \
            str(user.getResponse(userIn)) + \
            " \n                                                        ~"
        userIn = input(response)

    thankYou()


if __name__ == '__main__':  # executes the block at the start of the program , in this case it will execute Main()
    os.system("cls")

    Main()
    

    

    os.system("exit")
 