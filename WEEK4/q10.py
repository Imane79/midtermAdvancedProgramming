from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Open File Example")

# Create a label to show the file name
label = Label(root, text="No file chosen")
label.pack()

# Create a Text widget to show file content
text_box = Text(root, height=15, width=60)
text_box.pack()


def open_file():
    # Ask user to pick a file
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
        label.config(text=file_path)  # Show file path
        with open(file_path, "r") as file:
            content = file.read()
            text_box.delete("1.0", END)  # Clear previous content
            text_box.insert("1.0", content)  # Insert new content


# Button to trigger file open
button = Button(root, text="Open File", command=open_file)
button.pack()

root.mainloop()
