#Write a Python program to convert a tuple to a string.

def tuple_to_string(input_tuple):
    # Convert each element of the tuple to a string
    tuple_str = ''.join(map(str, input_tuple))
    return tuple_str

# Example usage:
my_tuple = (1, 2, 3, 4, 5)

# Convert tuple to string
result_string = tuple_to_string(my_tuple)

# Print the result
print("Tuple converted to string:", result_string)
