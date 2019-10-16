import tkinter as tk
import web
def getResponse(userIn):  # function that decides the appropriate response also our main

    subs = userIn.split()  # words
    if "weather" in subs:
        print ("gets weather")
        pass
    elif "date" in subs or "time" in subs:
        #return main.getDatetime()
        print ("gets time")
    elif "open" in subs or "search" in subs:
        for i in subs:
            if (i not in ["open", "search"]):
                web.openWeb(i)
                return "Opening "+i
    

class mainApp():
    
    def __init__(self):
        self.root = tk.Tk()
        self.HEIGHT = 1080
        self.WIDTH = 1920
        self.canvas = tk.Canvas(self.root, height=self.HEIGHT, width=self.WIDTH, bg='black')
        self.canvas.pack()

    

    def getInput(self):
        self.root.update()
        getResponse(self.entry_main.get())
    #def changeLabel(l, newText):
        #l["text"] = newText
        #return (l)

    def exitApp(self):
        self.root.destroy()
    
    
    def runMain(self):
        self.mainFrames()
        
        self.mainButton()
        self.mainEntry()
        self.mainLabels()
        self.mainScroll()
        self.root.mainloop()
        
        
    def mainFrames(self):
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.place(relx=0.7, relwidth=0.3, relheight=0.20)

        self.frame_display = tk.Frame(self.root, bg='white')
        self.frame_display.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.6)

        self.frame_dline = tk.Frame(self.root, bg='white')
        self.frame_dline.place(relx=0.8, rely=0.2, relwidth=0.3, relheight=0.299)

        self.frame_cal = tk.Frame(self.root, bg='white')
        self.frame_cal.place(relx=0.8, rely=0.5, relwidth=0.3, relheight=0.3)

        self.frame_tt = tk.Frame(self.root, bg='white')
        self.frame_tt.place(rely=0.2, relwidth=0.2, relheight=0.6)

        self.frame_image = tk.Frame(self.root, bg='white')
        self.frame_image.place(relx=0.37, rely=0.01, relwidth=0.2, relheight=0.1)

        self.frame_sugg = tk.Frame(self.root, bg='black')
        self.frame_sugg.place(rely=0.85, relwidth=1, relheight=0.1)

    def mainLabels(self):
        self.label1 = tk.Label(self.frame, text="WELCOME, USER",bg='black', fg='white', font=25)
        self.label1.pack()
        #  labels for calender --------->
        self.label_tt1 = tk.Label(self.frame_tt, text="Time table", font=20)
        self.label_tt1.place(rely=0.1, relheight=1, relwidth=1)

        self.label_dline = tk.Label(self.frame_dline, text="DEADLINES", fg='black', font=30)
        self.label_dline.place(relheight=1, relwidth=1)

        self.label_cal1 = tk.Label(self.frame_cal, text="CALENDER", font=15)
        self.label_cal1.place(relx=0.08, relheight=0.1, relwidth=0.5)

        self.label_cal2 = tk.Label(self.frame_cal)
        self.label_cal2.place(rely=0.1, relheight=0.9, relwidth=1)

        self.label_sugg = tk.Label(self.frame_sugg, text='Shortcuts: ',font=24, bg='black', fg='white')
        self.label_sugg.place(relwidth=0.14, relheight=0.3)

        self.label_main = tk.Label(self.frame_display)
        self.label_main.place(relwidth=1, relheight=0.95)

    def mainButton(self):
        # button for main display ---->

        self.button_main = tk.Button(self.frame_display, text="-->", bg='black', fg='white', activebackground='black',
                        activeforeground='white',command=self.getInput)
        self.button_main.place(rely=0.94, relx=0.9, relwidth=0.1, relheight=0.06)

        # buttons for calender ----->
        self.button_cal1 = tk.Button(self.frame_cal, text="<--", bg='#1f1f14',fg='white', activebackground='black', activeforeground='white')
        self.button_cal1.place(relx=0.0001, relheight=0.1, relwidth=0.1)

        self.button_cal1 = tk.Button(self.frame_cal, text="-->", bg='#1f1f14',
                        fg='white', activebackground='black', activeforeground='white')
        self.button_cal1.place(relx=0.55, relheight=0.1, relwidth=0.1)

        # buttons for time table ------->

        self.button_tt1 = tk.Button(self.frame_tt, text='<-- ', bg='#1f1f14', fg='white',
                       activebackground='black', activeforeground='white')
        self.button_tt1.place(relheight=0.1, relwidth=0.15)

        self.button_tt2 = tk.Button(self.frame_tt, text='  -->', bg='#1f1f14', fg='white',
                       activebackground='black', activeforeground='white')
        self.button_tt2.place(relx=0.85, relheight=0.1, relwidth=0.15)

        # suggestion buttons ------>
        self.button_openfile = tk.PhotoImage(file = 'button_open-file.png')
        self.button_sugg1 = tk.Button(self.frame_sugg, text='Suggestion 1', bg='black',
                         fg='white', activebackground='black', activeforeground='white', bd = 0, image = self.button_openfile)
        self.button_sugg1.place(relx=0.05, rely=0.45, relheight=0.45, relwidth=0.13)

        self.button_search = tk.PhotoImage(file = 'button_search.png')
        self.button_sugg2 = tk.Button(self.frame_sugg, text='Suggestion 2', bg='black',
                         fg='white', activebackground='black', activeforeground='white', bd = 0, image = self.button_search)
        self.button_sugg2.place(relx=0.25, rely=0.45, relheight=0.45, relwidth=0.12)

      
        self.button_sugg3 = tk.Button(self.frame_sugg, text='Suggestion 3', bg='black',
                         fg='white', activebackground='black', activeforeground='white', bd = 0,image=self.button_faculty_cont)
        self.button_sugg3.place(relx=0.45, rely=0.45, relheight=0.4, relwidth=0.15)
        self.button_messages= tk.PhotoImage(file='button_show-messages.png')
        self.button_sugg4 = tk.Button(self.frame_sugg, text='Suggestion 4', bg='black',
                         fg='white', activebackground='black', activeforeground='white', bd = 0,image=self.button_messages)
        self.button_sugg4.place(relx=0.65, rely=0.45, relheight=0.4, relwidth=0.15)
        
        self.button_power = tk.PhotoImage(file = 'power1.png')
        self.button_exit = tk.Button(self.frame_sugg, text="EXIT", bg='#1f1f14', fg='white',
                        activebackground='black', activeforeground='white', bd = 0,image = self.button_power,command=self.exitApp)
        self.button_exit.place(relx=0.85, rely=0.45, relheight=0.8, relwidth=0.08)

           
        # scrollbar for main window ------>
    def mainScroll(self):
        self.scroll1 = tk.Scrollbar(self.label_main, bg='blue')
        self.scroll1.place(relheight=1, relx=0.98)

    def mainEntry(self):
        self.entry_main = tk.Entry(self.frame_display, bg='white', fg='black')
        self.entry_main.place(rely=0.94, relwidth=0.9, relheight=0.06)

    
        

main = mainApp()
main.runMain()
