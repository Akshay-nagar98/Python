#Write a Python program to find the second smallest number in a list.

def second_smallest(numbers):
    # Initialize two variables to store smallest and second smallest numbers
    smallest = float('inf')
    second_smallest = float('inf')
    
    # Traverse the list to find the smallest and second smallest numbers
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    # Return the second smallest number found
    return second_smallest

# Example usage:
my_list = [8, 4, 9, 3, 6, 1, 5, 7]
second_min = second_smallest(my_list)
print("Second smallest number in the list:", second_min)
