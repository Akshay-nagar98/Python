#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    sum = 0
else:
    sum = num1 + num2 + num3

print("Sum of the three integers:", sum)
