#use this to test and run kivy gui
import kivy
from kivy.app import App
from kivy.uix.label import Label
from main import *


class mainApp(App):
    def build(self):
        return Label(text="Hello")
    
    
if __name__=="__main__":
    print ("hello")
    
    mainApp().run()
