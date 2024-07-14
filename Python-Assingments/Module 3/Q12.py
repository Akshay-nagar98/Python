#Write a Python program to convert a list of characters into a string.

def list_to_string(char_list):
    # Use the join() method to concatenate the characters into a string
    string_result = ''.join(char_list)
    return string_result

# Example usage:
char_list = ['H', 'e', 'l', 'l', 'o']
result_string = list_to_string(char_list)
print("List converted to string:", result_string)
