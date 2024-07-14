#Write a Python program to check whether a list contains a sub list

def is_sublist(main_list, sublist):
    # Convert lists to tuples to use in operator for sublist checking
    main_tuple = tuple(main_list)
    sublist_tuple = tuple(sublist)
    
    # Check if sublist is in main_list
    if sublist_tuple in main_tuple:
        return True
    else:
        return False

# Example usage:
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist1 = [2, 3, 4]
sublist2 = [5, 6, 10]

# Check if sublist1 is in main_list
if is_sublist(main_list, sublist1):
    print("sublist1 is present in main_list")
else:
    print("sublist1 is not present in main_list")

# Check if sublist2 is in main_list
if is_sublist(main_list, sublist2):
    print("sublist2 is present in main_list")
else:
    print("sublist2 is not present in main_list")
