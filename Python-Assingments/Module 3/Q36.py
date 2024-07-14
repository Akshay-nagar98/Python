#How Do You Check The Presence Of A Key In A Dictionary?

'''You can use the in keyword to check if a key exists in a dictionary. Here's how you can use it:'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check if 'a' is a key in my_dict
if 'a' in my_dict:
    print("'a' is present in the dictionary")
else:
    print("'a' is not present in the dictionary")

# Check if 'z' is a key in my_dict
if 'z' in my_dict:
    print("'z' is present in the dictionary")
else:
    print("'z' is not present in the dictionary")
