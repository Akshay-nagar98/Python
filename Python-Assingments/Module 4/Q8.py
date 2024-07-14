#Write a python program to find the longest words.


def find_longest_words(text):
    # Split the text into words
    words = text.split()
    
    # Initialize variables to store the longest words
    longest_words = []
    max_length = 0
    
    # Iterate through each word to find the longest ones
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_words = [word]
        elif word_length == max_length:
            longest_words.append(word)
    
    return longest_words

# Example usage:
input_text = "Python program to find the longest words in a sentence or text"
longest_words = find_longest_words(input_text)

# Print the longest words found
print("Longest words:", longest_words)
