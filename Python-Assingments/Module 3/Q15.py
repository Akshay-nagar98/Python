#Write a Python program to get unique values from a list

def get_unique_values(input_list):
    # Create an empty set to store unique values
    unique_values = set()

    # Add elements from input_list to the set (sets automatically handle duplicates)
    for item in input_list:
        unique_values.add(item)

    # Convert the set back to a list (if you need the result as a list)
    unique_list = list(unique_values)
    
    return unique_list

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 3, 6, 4, 7]
unique_values = get_unique_values(my_list)
print("Unique values from the list:", unique_values)
