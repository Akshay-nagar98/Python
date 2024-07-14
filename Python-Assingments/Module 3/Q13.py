#Write a Python program to select an item randomly from a list.

import random

def select_random_item(input_list):
    # Use random.choice() to select a random item from input_list
    random_item = random.choice(input_list)
    return random_item

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Select a random item from my_list
random_item = select_random_item(my_list)
print("Randomly selected item:", random_item)
