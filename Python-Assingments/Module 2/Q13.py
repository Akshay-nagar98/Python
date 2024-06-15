#Write a Python program to count the number of characters (character frequency) in a string

# Input the string
input_string = input("Enter a string: ")

# Count character frequency
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Display character frequency
for char, freq in char_frequency.items():
    print(f"Character '{char}' occurs {freq} times.")
