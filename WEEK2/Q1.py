file = open("dairy.txt", "w")
file.write("March 31, 2025\n")
file.write("Today I learned about file handling in Python.")
file.write("It was very interesting!")
#  do we have to close the file? why
# file.close()
# Yes, it is a good practice to close the file after writing to it.
# It ensures that all data is flushed from the buffer to the file and frees up system resources.
#  If you don't close the file, you may lose data or encounter file corruption.

file = open("dairy.txt", "r")
#  read the file and print its content
with open("dairy.txt", "r") as file:
    for line in file:
        print(line.strip())
#  read the file and print its content

#  here we are using the with statement to open the file, which automatically closes the file after the block is executed.

# What is the difference between opening a file in 'w' mode versus 'a' mode?
#  write mode is for creating a new file or overwriting an existing file,
#  while 'a' is for appending data to an existing file without overwriting it.

file = open("dairy.txt", "a")
file.write("\nI am excited to learn more about Python.")
#  so what was the difference between the two modes?
#  The difference is that 'w' mode overwrites the file if it exists, while 'a' mode appends to the file. which means it adds new content to the end of the file without deleting the existing content.
#  In 'w' mode, if the file already exists, it will be truncated to zero length before writing.

with open("dairy.txt", "r") as file:
    for line in file:
        print(line.strip())
