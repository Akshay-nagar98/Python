#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

def generate_square_list():
    # Generate squares of numbers between 1 and 30
    square_list = [i ** 2 for i in range(1, 31)]
    return square_list

def print_first_and_last_5(square_list):
    # Print first 5 elements
    print("First 5 elements:")
    print(square_list[:5])
    
    # Print last 5 elements
    print("Last 5 elements:")
    print(square_list[-5:])

# Generate square list
square_list = generate_square_list()

# Print first and last 5 elements
print_first_and_last_5(square_list)
