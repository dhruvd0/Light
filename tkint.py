import tkinter as tk
#import lms

root = tk.Tk()

HEIGHT = 1080
WIDTH = 1920

def main_input(say):
    print(say)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relx=0.7, relwidth=0.3, relheight=0.20)

frame_display = tk.Frame(root, bg='white')
frame_display.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.6)

frame_dline = tk.Frame(root, bg='white')
frame_dline.place(relx=0.8, rely=0.2, relwidth=0.3, relheight=0.299)

frame_cal = tk.Frame(root, bg='white')
frame_cal.place(relx=0.8, rely=0.5, relwidth=0.3, relheight=0.3)

frame_tt = tk.Frame(root, bg='white')
frame_tt.place(rely=0.2, relwidth=0.2, relheight=0.6)

frame_image = tk.Frame(root, bg='white')
frame_image.place(relx=0.37, rely=0.01, relwidth=0.2, relheight=0.1)

frame_sugg = tk.Frame(root, bg='black')
frame_sugg.place(rely=0.85, relwidth=1, relheight=0.1)


label_logo = tk.Label(frame_image, text="LOGO", fg='black', font=30)
label_logo.pack()

label_tt = tk.Label(frame_tt,text = "Time table", bg = 'green', font = 20)
label_tt.place(rely = 0.1, relheight = 1 , relwidth = 1)

label_dline = tk.Label(frame_dline, text="DEADLINES", fg='black', font=30)
label_dline.place(relheight=1,relwidth=1)

label_cal1 = tk.Label(frame_cal,text = "CALENDER", font = 15)
label_cal1.place(relx=0.08,relheight= 0.1, relwidth=0.5)

label_cal2 = tk.Label(frame_cal)
label_cal2.place(rely = 0.1 , relheight=0.9, relwidth=1)

label_sugg = tk.Label(frame_sugg, text = 'Suggestions: ', font = 20, bg = 'black', fg = 'white')
label_sugg.place(relwidth = 0.14 , relheight = 0.3)

label_main = tk.Label(frame_display)
label_main.place(relwidth = 1, relheight= 0.95 )

# --------------------------------------------------------------------------------------

label1 = tk.Label(frame, text="Username", bg='black', fg='white', font=25)
label1.pack()

entry_user = tk.Entry(frame, bg='#1f1f14', fg='white')
entry_user.pack()

label2 = tk.Label(frame, text="Password", bg='black', fg='white', font=25)
label2.pack()

entry_pass = tk.Entry(frame, bg='#1f1f14', fg='white')
entry_pass.pack()

def login():
    #lms.loginLms(entry_user.get(), entry_pass.get())
    pass


entry_main = tk.Entry(frame_display, bg = 'white', fg='black' )
entry_main.place(rely = 0.94, relwidth=0.9 , relheight = 0.06)

#button for main display ---->

button_main = tk.Button(frame_display,text = "-->", bg = 'black', fg = 'white',activebackground = 'black', activeforeground= 'white', command = lambda : main_input(entry_main.get()))
button_main.place(rely=0.94, relx = 0.9, relwidth = 0.1, relheight = 0.06)

#button for submit ------> 

button = tk.Button(frame, text="Submit", bg='#1f1f14',
                   fg='white', command=login,activebackground = 'black', activeforeground= 'white')
button.pack()

#buttons for calender ----->

button_cal1 = tk.Button(frame_cal, text = "<--", bg = '#1f1f14', fg = 'white', activebackground = 'black', activeforeground= 'white')
button_cal1.place(relx=0.0001, relheight = 0.1, relwidth= 0.1)

button_cal1 = tk.Button(frame_cal, text = "-->", bg = '#1f1f14', fg = 'white', activebackground = 'black', activeforeground= 'white')
button_cal1.place(relx=0.55, relheight = 0.1, relwidth= 0.1)

#buttons for time table ------->

button_tt1 = tk.Button(frame_tt,text = '<--', bg = '#1f1f14', fg = 'white', activebackground = 'black', activeforeground= 'white' )
button_tt1.place(relheight=0.1, relwidth = 0.15)

button_tt2 = tk.Button(frame_tt,text = '-->', bg = '#1f1f14', fg = 'white', activebackground = 'black', activeforeground= 'white' )
button_tt2.place(relx= 0.85, relheight=0.1, relwidth = 0.15)

#suggestion buttons ------>

button_sugg1 = tk.Button(frame_sugg, text = 'Suggestion 1', bg = '#1f1f14', fg = 'white', activebackground = 'black', activeforeground= 'white')
button_sugg1.place(relx= 0.05, rely=0.45,relheight= 0.4,relwidth=0.15)

button_sugg2 = tk.Button(frame_sugg, text = 'Suggestion 2', bg = '#1f1f14', fg = 'white',activebackground = 'black', activeforeground= 'white')
button_sugg2.place(relx= 0.25,rely=0.45,relheight= 0.4,relwidth=0.15)

button_sugg3 = tk.Button(frame_sugg, text = 'Suggestion 3', bg = '#1f1f14', fg = 'white',activebackground = 'black', activeforeground= 'white')
button_sugg3.place(relx=0.45 ,rely=0.45,relheight= 0.4,relwidth=0.15)

button_sugg4 = tk.Button(frame_sugg, text = 'Suggestion 4', bg = '#1f1f14', fg = 'white',activebackground = 'black', activeforeground= 'white')
button_sugg4.place(relx=0.65, rely=0.45,relheight= 0.4,relwidth=0.15)

while True:
    root.update()
