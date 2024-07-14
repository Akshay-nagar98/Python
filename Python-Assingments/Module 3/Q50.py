#Write a Python function to check whether a number is perfect or not.

def is_perfect_number(num):
    if num <= 0:
        return False
    
    sum_of_divisors = 0
    # Find all proper divisors (excluding the number itself)
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    # Check if the sum of divisors equals the number
    if sum_of_divisors == num:
        return True
    else:
        return False

# Example usage:
number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
