# Day 34: Graphical Interface

import tkinter

window = tkinter.Tk()
window.geometry("600x400")

text_field = tkinter.Entry(window)
text_field.pack()

label = tkinter.Label(window)
label.pack()


def get_text():
    text = text_field.get()
    label["text"] = text


button = tkinter.Button(window, text="Click", command=get_text)
button.pack()

window.mainloop()
