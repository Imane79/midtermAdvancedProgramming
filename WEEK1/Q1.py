#  if we use w we only write in the file if we try to read it we get an error
# now using w+ we can read and write in the file but we have to move the cursor to the beginning of the file

file = open("WEEk1/Q1.txt", 'w+')
file.write("Hello World")
file.write("\nThis is my first file")
file.seek(0)  # Move the cursor to the beginning of the file
# Read the file line by line
for line in file:
    print(line)
file.close()
