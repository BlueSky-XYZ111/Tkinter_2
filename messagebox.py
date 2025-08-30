from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Message window ")

def message():
    messagebox.showwarning("Alert window" , "There is a virus found here ! " , icon = "error")

btn = Button(root , command = message , text = "Scan for virus" , bg = "lightblue")
btn.pack()

root.mainloop()