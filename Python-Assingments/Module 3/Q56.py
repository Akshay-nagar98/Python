#How will you set the starting value in generating random numbers?

import random

# Set the seed value (starting value)
seed_value = 42
random.seed(seed_value)

# Generate some random numbers
random_number1 = random.randint(1, 100)
random_number2 = random.random()

print("Random number 1:", random_number1)
print("Random number 2:", random_number2)
