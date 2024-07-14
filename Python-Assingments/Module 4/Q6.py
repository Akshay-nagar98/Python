#Write a Python program to read a file line by line and store it into a list


def read_file_lines(file_name):
    try:
        lines = []
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Read each line and store in a list
            lines = file.readlines()
        
        return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []

# Example usage:
file_name = 'test.txt'

# Read file line by line and store in a list
file_lines = read_file_lines(file_name)

# Display the content of the list
print(f"Contents of '{file_name}':")
for line in file_lines:
    print(line.strip())  # Use strip() to remove newline characters

# Alternatively, you can print the entire list as well:
# print(file_lines)
