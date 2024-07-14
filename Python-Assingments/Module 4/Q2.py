#Write a Python program to read an entire text file.

def read_file(file_name):
    try:
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

# Example usage:
file_name = 'test.txt'
file_content = read_file(file_name)

print(f"Contents of '{file_name}':")
print(file_content)
