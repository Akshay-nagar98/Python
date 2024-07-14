#Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]
#Expected Output:
#Counter ({'item1': 1150, 'item2': 300})

from collections import Counter

def combine_values(list_of_dicts):
    combined = Counter()
    for d in list_of_dicts:
        combined[d['item']] += d['amount']
    return combined

# Sample data
data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300},
        {'item': 'item1', 'amount': 750}]

# Combine values and print the result
combined_values = combine_values(data)
print("Expected Output:")
print(combined_values)
