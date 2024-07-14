#How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

'''In Python, the try, except, and finally blocks are used together to handle exceptions and perform cleanup operations.'''

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print(f"The result of {x} divided by {y} is: {result}")
    finally:
        print("Executing finally block to clean up resources.")

# Example usage:
divide(10, 2)   # Normal execution
divide(10, 0)   # Exception occurs (ZeroDivisionError)
