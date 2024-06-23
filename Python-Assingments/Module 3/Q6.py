#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

def count_strings(strings):
  """Counts the number of strings in a list where the length is 2 or more and the first and last characters are the same.

  Args:
    strings: A list of strings.

  Returns:
    The number of strings that meet the criteria.
  """
  count = 0
  for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
      count += 1
  return count

# Example usage
strings = ["abc", "aba", "121", "xy", "madam", "hello"]
result = count_strings(strings)
print(f"Number of strings meeting the criteria: **{result}**")
