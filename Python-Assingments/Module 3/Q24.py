#Write a Python program to convert a list to a tuple.

def list_to_tuple(input_list):
    # Convert list to tuple using tuple() function
    output_tuple = tuple(input_list)
    return output_tuple

# Example usage:
input_list = [1, 2, 3, 4, 5]
output_tuple = list_to_tuple(input_list)
print("Original list:", input_list)
print("Converted tuple:", output_tuple)
