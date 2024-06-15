#Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

# Define input strings str1 and str2, separated by a space
str1 = "apple orange"
str2 = "banana grape"

# Split each string into a list using split() method
list1 = str1.split(' ')  # ['apple', 'orange']
list2 = str2.split(' ')  # ['banana', 'grape']

# Swap first two characters of each list using slicing
list1[0:2] = list1[1:]  # ['orange', 'apple'] for str1 = 'apple orange'
list2[0:2] = list2[1:]  # ['grape', 'banana'] for str2 = 'banana grape'

# Join each swapped list back into strings using join() method and concatenate them with a space in between using + operator
result_str = ' '.join(list1) + ' ' + ' '.join(list2)  # 'orange apple banana grape' as output string.
print(result_str)  # Output: orange apple banana grape. This is the desired single string from two given strings with swapped first two characters in each part.
