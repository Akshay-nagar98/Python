#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return math.pi * self.radius ** 2
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
# Create a Circle object with radius 5
circle1 = Circle(5)

# Compute the area and perimeter of circle1
area1 = circle1.compute_area()
perimeter1 = circle1.compute_perimeter()

print(f"Area of circle1: {area1:.2f}")  # Output: Area of circle1: 78.54
print(f"Perimeter of circle1: {perimeter1:.2f}")  # Output: Perimeter of circle1: 31.42

# Create another Circle object with radius 7
circle2 = Circle(7)

# Compute the area and perimeter of circle2
area2 = circle2.compute_area()
perimeter2 = circle2.compute_perimeter()

print(f"Area of circle2: {area2:.2f}")  # Output: Area of circle2: 153.94
print(f"Perimeter of circle2: {perimeter2:.2f}")  # Output: Perimeter of circle2: 43.98
