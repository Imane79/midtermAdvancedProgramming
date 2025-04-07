from tkinter import *

root = Tk()
root.title("Login Form")

# Username
username_label = Label(root, text="Username")
username_label.grid(row=0, column=0)

username_entry = Entry(root)
username_entry.grid(row=0, column=1)

# Password
password_label = Label(root, text="Password")
password_label.grid(row=1, column=0)

password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Login Button
login_button = Button(root, text="Login")
login_button.grid(row=2, column=0, columnspan=1)

root.mainloop()
