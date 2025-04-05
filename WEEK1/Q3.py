# === FILE HANDLING SUMMARY ===

# 📁 1. Writing to a file (clears contents if file exists!)
file = open("log.txt", "w")  # 'w' = write mode
file.write("it is iman\n")
file.write("hiiii\n")
file.close()

# 📁 2. Appending to a file (adds to the end, does NOT erase)
file = open("log.txt", "a")  # 'a' = append mode
file.write("another line\n")
file.close()

# 📁 3. Appending + Reading (we need to seek before reading!)
file = open("log.txt", "a+")
file.write("hello\n")
file.seek(0)  # move cursor to beginning of file to read
print("Contents of log.txt:")
print(file.read())
file.close()

# 📖 4. Reading all lines at once
file = open("log.txt", "r")
all_text = file.read()
print("Read all at once:")
print(all_text)
file.close()

# 🔁 5. Reading line-by-line using a loop
print("Read line-by-line:")
with open("log.txt", "r") as file:
    for line in file:
        print(line.strip())  # removes newline and extra spaces

# 🔍 6. Counting how many lines contain a word
keyword = "iman"
count = 0
with open("log.txt", "r") as file:
    for line in file:
        if line.strip() == keyword:  # strip is important here!
            count += 1
print(f'Lines that equal "{keyword}": {count}')

# 🧠 NOTES:
# - .strip() removes \n and spaces around text
# - .read() reads the whole file at once
# - .seek(0) resets the file's cursor back to the start
# - Use 'with open(...)' so you don't forget to close the file
# - Be careful using .read() more than once unless you seek()
