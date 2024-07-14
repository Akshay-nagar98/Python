#Write a Python program to remove duplicates from a list.


def remove_duplicates(input_list):
    # Create an empty list to store unique elements
    unique_list = []
    
    for item in input_list:
        # Add to unique_list only if the item is not already there
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Example usage:
input_list = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7,6,5,4]
print("Original list:", input_list)

unique_list = remove_duplicates(input_list)
print("List with duplicates removed:", unique_list)
