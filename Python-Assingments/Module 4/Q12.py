#Write a Python program to copy the contents of a file to another file.

def copy_file(source_file, destination_file):
    try:
        # Open source file in read mode and destination file in write mode
        with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
            # Read content from source file and write to destination file
            contents = src.read()
            dst.write(contents)
        
        print(f"Successfully copied contents from '{source_file}' to '{destination_file}'")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except IOError:
        print(f"Error: Could not write to file '{destination_file}'")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'

# Copy contents from source file to destination file
copy_file(source_file, destination_file)
