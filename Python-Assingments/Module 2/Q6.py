# Swapping with a temporary variable
a = 5
b = 10

temp = a
a = b
b = temp

print("After swapping with temp variable:")
print("a =", a)
print("b =", b)


# Swapping without a temporary variable
a = 5
b = 10

a, b = b, a

print("After swapping without temp variable:")
print("a =", a)
print("b =", b)
