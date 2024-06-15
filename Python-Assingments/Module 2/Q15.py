#Write a Python program to count occurrences of a substring in a string.

# Define the main string
main_string = "This is an example string with some repeated words in it."

# Define the substring to count occurrences of
substring = "is"

# Count and print the number of occurrences of the substring in the main string
occurrences = main_string.count(substring)
print("Number of occurrences of '{}' in the string: {}".format(substring, occurrences))
