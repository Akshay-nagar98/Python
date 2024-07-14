#Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_name):
    word_freq = {}
    
    try:
        # Open file in read mode
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            
            # Split the content into words (tokens)
            words = content.split()
            
            # Count frequency of each word
            for word in words:
                # Remove punctuation (if any)
                word = word.strip('.,!?"\'').lower()
                
                if word not in word_freq:
                    word_freq[word] = 0
                word_freq[word] += 1
        
        return word_freq
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return {}
    
# Example usage:
file_name = 'test.txt'

# Count word frequency in the file
word_frequency = count_word_frequency(file_name)

# Display the word frequencies
print(f"Word frequencies in '{file_name}':")
for word, freq in word_frequency.items():
    print(f"{word}: {freq}")
