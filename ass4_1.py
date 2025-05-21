filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        print(f"Contents of '{filename}':")
        for line in file:
            print(line, end='')  # end='' prevents adding extra newline
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
