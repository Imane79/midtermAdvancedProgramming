# Write a program that reads the file, calculates each student's average grade,
# and writes the results to a new file "averages.txt" in the format:
# Alice:90,85,92,78
# Bob:88,76,95,82
# Charlie:75,80,88,92

with open("grades.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")
        if len(parts) != 2:
            print(f"Invalid line format: {line}")
            continue
        name = parts[0]
        grades = parts[1]
        # convert grades to a list of integers
        grades_values = []
        for grade in grades.split(","):
            try:
                grades_values.append(int(grade))
            except ValueError:
                print(f"Invalid grade value: {grade}")
                continue

            if grades_values:
                average = sum(grades_values) / len(grades_values)
                print(f"{name}: {average:.2f}")

# Write a program that reads the file, calculates each student's average grade,

with open("grades.txt", "r") as input_file, open("averages.txt", "w") as output_file:
    for line in input_file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(":")
        if len(parts) != 2:
            print(f"Invalid line format: {line}")
            continue

        name = parts[0]
        grades_str = parts[1]

        # Convert all grades first
        grades = []
        for grade in grades_str.split(","):
            try:
                grades.append(int(grade))
            except ValueError:
                print(f"Invalid grade value for {name}: {grade}")
                continue

        # Then calculate average AFTER all grades are processed
        if grades:
            average = sum(grades) / len(grades)
            output_file.write(f"{name}: {average:.2f}\n")
            print(f"{name}: {average:.2f}")  # Optional: print to console too
