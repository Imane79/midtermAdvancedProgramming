from tkinter import *

root = Tk()
root.title("Notepad with Button")

# Create a Text widget
text = Text(root, height=10, width=40)
text.pack(pady=10)

# Define a function to print what’s typed


def show_text():
    content = text.get("1.0", END)  # get from line 1, char 0 to end
    print(content)


# Add a button to call the function
button = Button(root, text="Print Text", command=show_text)
button.pack(pady=5)

root.mainloop()
