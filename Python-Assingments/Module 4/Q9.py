#Write a Python program to count the number of lines in a text file.

def count_lines(file_name):
    try:
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Initialize line counter
            line_count = 0
            
            # Iterate through each line and count them
            for line in file:
                line_count += 1
        
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return -1  # Return -1 or any suitable value to indicate error

# Example usage:
file_name = 'test.txt'

# Count the number of lines in the file
num_lines = count_lines(file_name)

# Display the number of lines
if num_lines != -1:
    print(f"Number of lines in '{file_name}': {num_lines}")
