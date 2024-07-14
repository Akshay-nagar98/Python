#Write a Python program to print all unique values in a dictionary. 

# Create a list 'L' containing dictionaries with key-value pairs.
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

# Print a message indicating the start of the code section.
print("Original List: ", L)

# Create a set 'u_value' to store unique values found in the dictionaries within the list 'L'.
# Use a set comprehension to iterate through the dictionaries and values and extract unique values.
u_value = set(val for dic in L for val in dic.values())

# Print the unique values stored in the 'u_value' set.
print("Unique Values: ", u_value) 
