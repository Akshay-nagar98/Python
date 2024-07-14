#Write a Python program to split a list into different variables.

def split_list_to_variables(input_list):
    # Unpack the list into separate variables
    var1, var2, var3 = input_list
    
    return var1, var2, var3

# Example usage:
my_list = [1, 2, 3]

# Split the list into variables
result1, result2, result3 = split_list_to_variables(my_list)

# Print the variables
print("Variable 1:", result1)
print("Variable 2:", result2)
print("Variable 3:", result3)
