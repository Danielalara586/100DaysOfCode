# Day 40: Login Screen

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.geometry('350x500')
window.title('Login')
window.resizable(0, 0)

j = 0
r = 0

for i in range(100):
    c = str(222222 + r)
    Frame(window, width=10, height=500, bg='#' + c).place(x=j, y=0)
    j += 10
    r += 1

Frame(window, width=250, height=400, bg='white').place(x=50, y=50)

label1 = Label(window, text='Username', bg='white')
typography = ('Verdana', 13)
label1.config(font=1)
label1.place(x=80, y=200)

entry1 = Entry(window, width=20, border=0)
entry1.config(font=1)
entry1.place(x=80, y=230)

label2 = Label(window, text='Password', bg='white')
typography = ('Verdana', 13)
label2.config(font=1)
label2.place(x=80, y=280)

entry2 = Entry(window, width=20, border=0)
entry2.config(font=1)
entry2.place(x=80, y=310)

Frame(window, width=180, height=2, bg='#141414').place(x=80, y=250)
Frame(window, width=180, height=2, bg='#141414').place(x=80, y=330)

image1 = Image.open("log.PNG")
image2 = ImageTk.PhotoImage(image1)

label3 = Label(image=image2, border=0, justify=CENTER)
label3.place(x=115, y=50)


def cmd():
    if entry1.get() == 'programmed' and entry2.get() == 'programmed':
        messagebox.showinfo('LOGIN SUCCESSFULLY\t\t WELCOME')
    else:
        messagebox.showinfo('LOGIN FAILED\t\t PLEASE TRY AGAIN')


Button(window, width=20, height=2, fg='black', bg='#994422', border=0, command=cmd, text='Login').place(x=100, y=375)


window.mainloop()
