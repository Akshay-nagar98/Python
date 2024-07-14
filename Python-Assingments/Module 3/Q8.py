#Write a Python program to check a list is empty or not

def is_list_empty(input_list):
    # Check if the list is empty
    if not input_list:
        return True
    else:
        return False

# Example usage:
empty_list = []
non_empty_list = [1, 2, 3]

# Check if empty_list is empty
if is_list_empty(empty_list):
    print("empty_list is empty")
else:
    print("empty_list is not empty")

# Check if non_empty_list is empty
if is_list_empty(non_empty_list):
    print("non_empty_list is empty")
else:
    print("non_empty_list is not empty")
