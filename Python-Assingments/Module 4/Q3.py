#Write a Python program to append text to a file and display the text.

def append_to_file(file_name, text_to_append):
    try:
        # Open file in append mode ('a')
        with open(file_name, 'a') as file:
            # Append text to the file
            file.write(text_to_append + '\n')
        
        # Read the entire content of the file again
        with open(file_name, 'r') as file:
            updated_content = file.read()
        
        return updated_content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

# Example usage:
file_name = 'test.txt'
text_to_append = "Additional line appended to the file."

# Append text to the file and display the updated content
updated_content = append_to_file(file_name, text_to_append)

print(f"Updated content of '{file_name}':")
print(updated_content)
