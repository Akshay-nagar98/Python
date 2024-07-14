#Write a Python program to read last n lines of a file.

def read_last_n_lines(file_name, n):
    try:
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Read all lines into a list
            lines = file.readlines()
        
        # Extract the last n lines
        last_n_lines = lines[-n:]

        return ''.join(last_n_lines)  # Return as a single string
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

# Example usage:
file_name = 'test.txt'
n = 3

# Read last n lines from the file
last_n_lines = read_last_n_lines(file_name, n)

print(f"Last {n} lines of '{file_name}':")
print(last_n_lines)
