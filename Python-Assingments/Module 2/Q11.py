#Write a python program to sum of the first n positive integers.

n = int(input("Input a number: "))
# Calculate the sum of the first 'n' positive integers using the formula.
sum_num = (n * (n + 1)) / 2
# Print the result, indicating the sum of the first 'n' positive integers.
print("Sum of the first", n, "positive integers:", sum_num)
