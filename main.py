from tkinter import * 
from PIL import Image , ImageTk

root = Tk()
root.title("Adding Image....")
root.geometry("1000x1000")

image1 = Image.open("image.png")
upload = ImageTk.PhotoImage(image1)

label = Label(root, image = upload , width = 500 , height = 500)
label.place(x = 0 , y = 0)
label2 = Label(root, text = "This is the image .....")
label2.place(x = 0 , y = 0)
root.mainloop()