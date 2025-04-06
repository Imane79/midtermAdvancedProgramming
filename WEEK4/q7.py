from tkinter import *

root = Tk()
root.title("Listbox Example")

# Step 1: Create a Listbox widget
listbox = Listbox(root)

# Step 2: Insert items into the listbox
listbox.insert(END, "Python")
listbox.insert(END, "Java")
listbox.insert(END, "C++")

# Step 3: Pack the Listbox so it appears in the window
listbox.pack()

root.mainloop()
