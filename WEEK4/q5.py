# checkbox
from tkinter import *

root = Tk()
root.geometry("400x150")
label = Label(root, text="do you agree?")
label.pack()

# 🔹 Create an IntVar to track the checkbox (0 = off, 1 = on)
agree_var = IntVar()

# 🔹 Create the checkbox
# check = Checkbutton(root, text="I agree", variable=agree_var)
check = Checkbutton(root, text="agree", variable=agree_var)
check.pack()
# 🔹 Label to show result
label_empty = Label(root, text="")
label_empty.pack()

# 🔹 Button to submit answer


def opinion():
    if agree_var.get() == 1:
        label_empty.config(text="you agree!")
    else:
        label_empty.config(text="disagree!")


button = Button(root, text="submit", command=opinion)
button.pack()

root.mainloop()
