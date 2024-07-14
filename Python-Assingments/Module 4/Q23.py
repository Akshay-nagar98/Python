#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def compute_area(self):
        return self.length * self.width

# Example usage:
# Create a Rectangle object with length 5 and width 3
rectangle1 = Rectangle(5, 3)

# Compute the area of rectangle1
area1 = rectangle1.compute_area()
print(f"Area of rectangle1: {area1}")  # Output: Area of rectangle1: 15

# Create another Rectangle object with length 7 and width 4
rectangle2 = Rectangle(7, 4)

# Compute the area of rectangle2
area2 = rectangle2.compute_area()
print(f"Area of rectangle2: {area2}")  # Output: Area of rectangle2: 28
