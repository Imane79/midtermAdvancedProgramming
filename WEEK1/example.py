# File contains: "  Hello  \n  World  \n"
with open("demo.txt") as f:
    print("Raw:")
    f.seek(0)
    for line in f:
        print(repr(line))  # Shows escape chars

    print("\nprint(line):")
    f.seek(0)
    for line in f:
        print(line)  # Double-spaced with indentation

    print("\nprint(line.strip()):")
    f.seek(0)
    for line in f:
        print(line.strip())  # Clean single lines

    print("\nprint(line, end=''):")
    f.seek(0)
    for line in f:
        print(line, end='')  # Keeps whitespace, single-spaced
