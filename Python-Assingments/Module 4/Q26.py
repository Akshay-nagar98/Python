#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?


'''Inheritance is a fundamental concept in object-oriented programming (OOP) where a new class (derived class or subclass)
is created from an existing class (base class or superclass).The derived class inherits attributes
and methods from the base class, allowing for code reuse and hierarchical organization of classes.'''

# Base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class (subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (subclass)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods defined in the base class through subclasses
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!



