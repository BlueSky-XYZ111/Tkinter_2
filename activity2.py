from tkinter import *

root = Tk()
root.title("The Main Window")
root.geometry("500x500")

l = Label(root , text = "This is the main window ....." , fg = "blue")
l.pack()

def topWindow() :

    top = Toplevel()
    top.title("New Window")
    top.geometry("200x200")

    label = Label(top , text = "This is the second (new) window . ")
    label.pack()
    top.mainloop()

btn = Button(root , text = "Click to open new window !" , bg = "lightblue" , command = topWindow)
btn.pack()

root.mainloop()

