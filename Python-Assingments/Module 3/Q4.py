#Write a Python function to get the largest number, smallest num and sum of all from a list.

def get_largest_smallest_sum(numbers):
  """
  This function takes a list of numbers and returns the largest number, smallest number, and sum of all numbers in the list.

  Args:
    numbers: A list of numbers.

  Returns:
    A tuple containing the largest number, smallest number, and sum of all numbers in the list.
  """
  if not numbers:
    return None, None, None

  largest = numbers[0]
  smallest = numbers[0]
  sum = 0

  for number in numbers:
    if number > largest:
      largest = number
    if number < smallest:
      smallest = number
    sum += number

  return largest, smallest, sum
