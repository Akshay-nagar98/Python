#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def check_integer_values(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

# Test cases
print(check_integer_values(2, 3))   # False
print(check_integer_values(2, 2))   # True
print(check_integer_values(7, 2))   # True
print(check_integer_values(10, 5))  # True
