#Write a Python program to reverse a tuple.

def reverse_tuple(input_tuple):
    # Convert tuple to a list, reverse the list, then convert back to tuple
    reversed_tuple = tuple(reversed(input_tuple))
    return reversed_tuple

# Example usage:
input_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(input_tuple)
print("Original tuple:", input_tuple)
print("Reversed tuple:", reversed_tuple)
