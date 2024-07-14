#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

class Car:
    # Class attribute
    wheels = 4
    
    # Constructor (initializer) method
    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year
    
    # Instance method to display car information
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}, {self.wheels} wheels")
    
    # Instance method to change the car model
    def change_model(self, new_model):
        self.model = new_model
        print(f"Model changed to: {self.model}")

# Creating instances (objects) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)

# Accessing instance attributes and calling methods
car1.display_info()  # Output: Car: 2020 Toyota Camry, 4 wheels
car2.change_model("Civic")  # Output: Model changed to: Civic
car2.display_info()  # Output: Car: 2021 Honda Civic, 4 wheels
