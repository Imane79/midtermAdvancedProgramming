
from tkinter import *

root = Tk()
root.title("hii")
root.geometry("400x100")

label = Label(root, text="click on the button is you agree!")
label.pack()

# creat an empty label
opinion_label = Label(root, text="")
opinion_label.pack()


def agree():
    opinion_label.config(text="you agree!")


def disagree():
    opinion_label.config(text="you disagree!")


button1 = Button(root, text="agree", command=agree)
button1.pack()
button2 = Button(root, text="disagree", command=disagree)
button2.pack()
root.mainloop()
