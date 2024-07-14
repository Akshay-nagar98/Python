#Write a Python program to map two lists into a dictionary

# Create a list 'keys' containing color names.
keys = ['red', 'green', 'blue']

# Create another list 'values' containing corresponding color codes in hexadecimal format.
values = ['#FF0000', '#008000', '#0000FF']

# Use the 'zip' function to pair each color name with its corresponding color code and create a list of tuples.
# Then, use the 'dict' constructor to convert this list of tuples into a dictionary 'color_dictionary'.
color_dictionary = dict(zip(keys, values))

# Print the resulting 'color_dictionary' containing color names as keys and their associated color codes as values.
print(color_dictionary)
