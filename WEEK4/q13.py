from tkinter import *

root = Tk()
root.title("Frame Example")

# Create top frame
top_frame = Frame(root)
top_frame.pack()

# Add a label and a button inside the top frame
label1 = Label(top_frame, text="Welcome!")
label1.pack(side=LEFT)

button1 = Button(top_frame, text="Click Me")
button1.pack(side=LEFT)

# Create bottom frame
bottom_frame = Frame(root)
bottom_frame.pack()

# Add a label in the bottom frame
label2 = Label(bottom_frame, text="Ready")
label2.pack()

root.mainloop()
