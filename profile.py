import web
import main
import lms

# use this file to get user Response and manipulate user profile and data


def getResponse(userIn):  # function that decides the appropriate response also our main

    subs = userIn.split()  # words
    if "weather" in subs:
        #return web.getWeather()
        pass
    elif "date" in subs or "time" in subs:
        return main.getDatetime()
    elif "open" in subs or "search" in subs:
        for i in subs:
            if (i not in ["open", "search"]):
                web.openWeb(i)
                return "Opening "+i
    elif "lms" in subs or "login" in subs:
        lms.loginLms()

