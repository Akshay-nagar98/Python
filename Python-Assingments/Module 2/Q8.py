#Write a Python program to test whether a passed letter is a vowel or not.

def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter in vowels:
        return f"The character '{letter}' is a vowel!"
    else:
        return f"The character '{letter}' is a consonant!"

# Test the function with different letters
print(is_vowel('a'))
print(is_vowel('O'))
print(is_vowel('k'))
