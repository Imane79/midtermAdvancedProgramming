from tkinter import *
# 1. Create the main window (root)
root = Tk()

# 2. Set title and size
root.title("title")
root.geometry("800x400")  # Optional
label = Label(root, text="Enter your name")
label.pack()
entry = Entry(root)
entry.pack()

# this will appear on the terminal


def greet():
    name = entry.get()
    print(f"Hello, {name}")


# this is the button when we click on it we will get we asked what
# we asked to print
button = Button(root, text="say hello! ", command=greet)
button.pack()
root.mainloop()
