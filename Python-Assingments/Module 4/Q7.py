#Write a Python program to read a file line by line store it into a variable.

def read_file_content(file_name):
    try:
        content = ''
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Read each line and concatenate into a single string
            for line in file:
                content += line
        
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return ''

# Example usage:
file_name = 'test.txt'

# Read file line by line and store in a variable
file_content = read_file_content(file_name)

# Display the content of the variable
print(f"Contents of '{file_name}':")
print(file_content)
