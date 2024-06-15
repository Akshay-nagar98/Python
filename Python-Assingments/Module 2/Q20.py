#Write a Python function that takes a list of words and returns the length of the longest one

def find_longest_word(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

# Test the function
word_list = ["apple", "banana", "cherry", "date"]
result = find_longest_word(word_list)
print(result)
