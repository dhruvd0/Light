import os #os.system(string) is used to run cmd commands 
userIn=""

def welcome(): #welcome screen
    print("                                                            WELCOME \n \n")
    userIn = input(
        "                            Ask me Anything \n                                                        ~ ")

def checkIn():
    for x in userIn:
        if x.isalpha()==False:
            print ("string is not valid")
    else:
        print ("                        Sure i can do that")
    
def checkDictionary():
    pass

def getWeather():
    pass

def getDatetime():
    pass    

def openApps():
    pass

def showSchedule():
    pass         
def Main():  # all the functions will be called here
    welcome()
    checkIn()
    checkDictionary()
    getWeather()
    getDatetime()
    openApps()
    showSchedule()


if __name__ == '__main__':  # executes the block at the start of the program , in this case it will execute Main()
    os.system("cls")
    Main()
