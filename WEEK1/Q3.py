
file = open("WEEK1/Q2.txt", 'r')
print(file.readline())  # Print the first line
with open("WEEK1/Q2.txt", 'r') as file:
    for line in file:
        #  here we are using a for loop to iterate through each line in the file
        print(line.strip())  # Print each line without the newline character
#  this is a more efficient way to read a file line by line
#  since we don't need to close the file manually
