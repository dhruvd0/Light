import os  # os.system(string) is used to run cmd commands
userIn = ""  # global user input


def checkIn():  # checks if user input is alphanumeric
    for x in userIn:
        if x.isalpha() == False:
            print("string is not valid")
    else:
        print("                                  Sure i can do that")


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


def thankYou():
    print ("\n Thank you \n")    
    print ("\n Version : 1.0.0 ")
    print ("Support : https://github.com/dhruvd0/End-Sem-Project \n")
    


def getResponse():
    return ("sure i can do that")


def Main():  # main display and user input 
    print("                                                            WELCOME \n \n")
    userIn=input("                            Ask me Anything \n                                                        ~ ")
    exit_op = ["quit", "bye", "ttly", "exit", ]
    while(True):
        if userIn in exit_op:
                
            break
        response="\n                            "+ getResponse() +" \n                                                        ~"
        userIn=input(response)
    thankYou()


if __name__ == '__main__':  # executes the block at the start of the program , in this case it will execute Main()
    os.system("cls")

    Main()
    os.system("exit")
   
    
