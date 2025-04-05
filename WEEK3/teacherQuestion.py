# 1. Write a Python script that lists all files and directories in the current working
# directory.

import os
# current working directory
cwd = os.getcwd()

print(os.listdir(cwd))

# Create a new directory named "backup" if it doesn't already exist.
# os.mkdir("backup")

# Write a function that checks if a file named "data.txt" exists in the current directory.
os.path.isfile("data.txt")


def checkfile():
    return os.path.isfile("data.txt")


print(checkfile)

#  Write a script that renames all files with the extension ".txt" to have a ".bak"
# extension

for file in os.listdir():
    if file.endswith(".text") and os.path.isfile(file):
        new = file.replace(".txt", ".bak")
        os.rename(file, new)
