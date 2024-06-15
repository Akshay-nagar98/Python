#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def replace_not_poor(input_str):
    index_not = input_str.find('not')
    index_poor = input_str.find('poor')

    if index_not != -1 and index_poor != -1 and index_not < index_poor:
        return input_str.replace(input_str[index_not:index_poor+4], 'good')
    else:
        return input_str

# Test the function
input_string = "The weather is not that poor, but not great either."
result = replace_not_poor(input_string)
print(result)
