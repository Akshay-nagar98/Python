#Write a Python program to write a list to a file.

def write_list_to_file(file_name, data_list):
    try:
        # Open file in write mode
        with open(file_name, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')  # Write each item to a new line
        print(f"Successfully wrote {len(data_list)} items to '{file_name}'")
    except IOError:
        print(f"Error writing to file '{file_name}'")

# Example list to write to file
data = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Example usage:
file_name = 'test.txt'

# Write the list to the file
write_list_to_file(file_name, data)
