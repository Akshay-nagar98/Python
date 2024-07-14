#Write a Python function that takes two lists and returns true if they have at least one common member.

def have_common_member(list1, list2):
    # Convert lists to sets for efficient membership checking
    set1 = set(list1)
    set2 = set(list2)
    
    # Check for intersection of the two sets
    if set1.intersection(set2):
        return True
    else:
        return False

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

if have_common_member(list1, list2):
    print("Lists have at least one common member")
else:
    print("Lists do not have any common member")
