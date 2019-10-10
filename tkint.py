import tkinter as tk
root = tk.Tk()

HEIGHT = 700
WIDTH = 800

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH, bg = 'black')
canvas.pack()

frame = tk.Frame(root, bg = 'black')
frame.place(relx=0.7 , relwidth=0.3, relheight = 0.20) 

label_main = tk.Label(root, text = "Light", bg = 'white', fg = 'white')
label_main.pack()

label1 = tk.Label(frame, text = "Username", bg = 'black', fg = 'white', font = 25)
label1.pack() 

entry_user = tk.Entry(frame , bg = '#1f1f14', fg = 'white')
entry_user.pack()

label2 = tk.Label(frame, text = "Password", bg = 'black', fg = 'white', font = 25)
label2.pack()

entry_pass = tk.Entry(frame, bg = '#1f1f14', fg = 'white')
entry_pass.pack()

button = tk.Button(frame , text="Submit", bg = '#1f1f14', fg = 'white')
button.pack()


root.mainloop() 