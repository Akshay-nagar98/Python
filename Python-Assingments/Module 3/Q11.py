#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def get_unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    # Iterate through the input_list
    for item in input_list:
        # Add to unique_list only if the item is not already there
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("Original list:", original_list)

unique_list = get_unique_elements(original_list)
print("List with unique elements:", unique_list)
