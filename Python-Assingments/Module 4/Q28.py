#What is used to check whether an object o is an instance of class A?

# Define a class A
class A:
    pass

# Create an object of class A
obj = A()

# Check if obj is an instance of class A
if isinstance(obj, A):
    print("obj is an instance of class A")
else:
    print("obj is not an instance of class A")
