#Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']}
#Expected Output:
#ac ad bc bd

from itertools import product

def generate_combinations(data):
    # Extract lists of letters from the dictionary values
    lists_of_letters = [data[key] for key in data]
    
    # Generate combinations using itertools.product
    combinations = list(product(*lists_of_letters))
    
    # Convert tuples to strings and join them
    result = [''.join(comb) for comb in combinations]
    
    return result

# Sample data
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Generate and display combinations
combinations = generate_combinations(data)
print("Expected Output:")
print(' '.join(combinations))
