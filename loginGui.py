import tkinter as tk1

side = tk1.Tk()

HEIGHT = 500
WIDTH = 550

canvas = tk1.Canvas(side, height=HEIGHT, width=WIDTH, bg='black')
canvas.pack()

frame = tk1.Frame(side, bg='black')
frame.place(relwidth=1, relheight=1)

label_logo = tk1.Label(frame, text="LIGHT", fg='white', font=1000, bg = 'black')
label_logo.place(relx = 0.4, relheight = 0.2, relwidth= 0.2)

label1 = tk1.Label(frame, text="Username: ", bg='black', fg='white', font=25)
label1.place(relx = 0.15,rely = 0.4)

entry_user = tk1.Entry(frame, bg='#1f1f14', fg='white')
entry_user.place(relx=0.4, rely = 0.41, relheight = 0.05, relwidth = 0.5)

label2 = tk1.Label(frame, text="Password: ", bg='black', fg='white', font=25)
label2.place(relx = 0.15, rely = 0.5,)

entry_pass = tk1.Entry(frame, bg='#1f1f14', fg='white')
entry_pass.place(relx=0.4, rely = 0.51, relheight = 0.05, relwidth = 0.5)

button = tk1.Button(frame, text="Submit", bg='#1f1f14',fg='white',activebackground = 'black', activeforeground= 'white')
button.place(relx = 0.5 , rely = 0.61, relheight= 0.05, relwidth = 0.2)

side.mainloop()