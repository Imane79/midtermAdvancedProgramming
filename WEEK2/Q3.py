# Write a Python program that reads a text file named "input.txt",
# reverses the order of its lines, and writes the result to a
# new file named "reversed.txt". Additionally, within each line,
# reverse the order of the words (but keep the words themselves unchanged).

def reverse_file_content(input_filename, output_filename):
    """
    Reverses the order of lines and words in a text file.

    Args:
        input_filename: Path to the input file
        output_filename: Path for the output file
    """
    try:
        # 1. Read the input file
        with open(input_filename, 'r') as input_file:
            # Read all lines and remove any surrounding whitespace (including newlines)
            lines = [line.strip() for line in input_file.readlines()]

        # 2. Process each line: reverse line order AND word order
        reversed_lines = []
        for line in reversed(lines):  # Process lines from last to first
            words = line.split()      # Split into individual words
            reversed_words = ' '.join(reversed(words))  # Reverse word order
            reversed_lines.append(reversed_words)

        # 3. Write to output file
        with open(output_filename, 'w') as output_file:
            # Join all reversed lines with newline characters
            output_file.write('\n'.join(reversed_lines))

        print(f"Success! Reversed content saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except PermissionError:
        print(f"Error: No permission to write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Example usage:
reverse_file_content("input.txt", "reversed.txt")
