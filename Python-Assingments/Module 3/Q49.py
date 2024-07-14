#Write a Python function to check whether a number is in a given range

def in_range(num, start, end):
    # Check if num is within the range [start, end]
    if start <= num <= end:
        return True
    else:
        return False

# Example usage:
number = 7
range_start = 1
range_end = 10

# Check if number is in the specified range
if in_range(number, range_start, range_end):
    print(f"{number} is in the range [{range_start}, {range_end}]")
else:
    print(f"{number} is not in the range [{range_start}, {range_end}]")
