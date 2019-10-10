import tkinter as tk
import os
import notifs
import webbrowser
import requests
import urllib
import web
from getpass import getpass
from bs4 import BeautifulSoup
import wget
import tkint
import lms

root = tk.Tk()

HEIGHT = 1080
WIDTH = 1920

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

frame_sugg = tk.Frame(root, bg='white')
frame_sugg.place(rely=0.85, relwidth=1, relheight=0.1)


label_logo = tk.Label(frame_image, text="LOGO", fg='black', font=30)
label_logo.pack()

label_tt = tk.Label(frame_tt, text="TIME TABLE", fg='black', font=30)
label_tt.pack()

label_dline = tk.Label(frame_dline, text="DEADLINES", fg='black', font=30)
label_dline.pack()

label_cal = tk.Label(frame_cal, text="CALENDER", fg='black', font=30)
label_cal.pack()

label_sugg = tk.Label(frame_sugg, text="SUGGESTIONS", fg='black', font=30)
label_sugg.pack()

label_main = tk.Label(frame_display, text="MAIN WINDOW", fg='black', font=30)
label_main.pack()

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
    lms.loginLms(entry_user.get(), entry_pass.get())



button = tk.Button(frame, text="Submit", bg='#1f1f14',
                   fg='white', command=login)
button.pack()

while True:
    root.update()
