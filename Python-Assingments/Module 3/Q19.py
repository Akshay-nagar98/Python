#Write a Python program to create a tuple with different data types.

# Creating a tuple with different data types
mixed_tuple = (1, 'hello', 3.14, True, [5, 6, 7])

# Printing the tuple
print("Mixed tuple:", mixed_tuple)

# Accessing elements of the tuple
print("Elements of the tuple:")
for element in mixed_tuple:
    print(element, " - Type:", type(element))
