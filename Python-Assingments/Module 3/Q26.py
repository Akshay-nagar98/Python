#Write a Python program to replace last value of tuples in a list.

def replace_last_value(tuples_list, new_value):
    modified_tuples = []
    for tup in tuples_list:
        # Create a new tuple with the last value replaced by new_value
        modified_tuple = tup[:-1] + (new_value,)
        modified_tuples.append(modified_tuple)
    return modified_tuples

# Example usage:
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10
modified_tuples = replace_last_value(tuples_list, new_value)

print("Original list of tuples:", tuples_list)
print("Modified list of tuples:", modified_tuples)
