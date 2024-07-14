#Write a Python program to check whether an element exists within a tuple.

def element_exists_in_tuple(input_tuple, element):
    # Check if element exists in input_tuple
    if element in input_tuple:
        return True
    else:
        return False

# Example usage:
my_tuple = (1, 2, 3, 4, 5)

# Check if element exists in the tuple
element_to_check = 3
if element_exists_in_tuple(my_tuple, element_to_check):
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")
