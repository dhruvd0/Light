import webbrowser



#This particular method is called "Web scraping"



#Use this file to test and learn requests and Beautiful soup


import requests
import urllib
from bs4 import BeautifulSoup

url="https://www.google.com"
r=requests.get(url) #use this get webpages , returns 200

#rint (r.content) #gets raw html data in text form

soup = BeautifulSoup(r.content, 'html5lib')  #html5lib is a parser , Beautiful Soup creates an Html object

links=soup.find_all("input",attrs={"name:q"}) #scraped all link elements from google.com



def checkDictionary():
    pass


def getWeather():
    return ("shows weather")

def openWeb(link):#checks if the links is valid
    mainLink=link
    if (link[0:12]!="http://www."):
        temp="http://www."
        temp=temp+link
        link=temp
    try:
        request=requests.get(link)  
            
    except requests.exceptions.MissingSchema:
        link="https://www.google.com/search?q="+mainLink
        
    except requests.exceptions.ConnectionError:
        link="https://www.google.com/search?q="+mainLink
    webbrowser.open(link)
    

      

if __name__=="__main__":
    openWeb("hello")

   
