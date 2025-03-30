# File Creation & Writing
# Write a program that creates a file called notes.txt and writes three lines:

# Copy
# Lecture 1: File Handling
# Date: 2024-03-15
# Topic: Python I/O

file = open("WEEK1/Q2.txt", 'w')
file.write("Lecture 1: File Handling\n")
file.write("Date: 2024-03-15\n")
file.write("Topic: Python I/O\n")
file.close()
# File Reading
file = open("WEEK1/Q2.txt", 'r')
file.readline()  # Read the first line
print(file.readline())  # Print the first line

# each time we use readline() it reads the next line
#  since we used readline() for the first time it reads the first line but we
#  only print the second line
