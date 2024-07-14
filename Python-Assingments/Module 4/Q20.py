#Write python program that user to enter only odd numbers, else will raise an exception.

def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 == 0:
                raise ValueError("Even number entered. Please enter an odd number.")
            else:
                print(f"You entered: {num}")
                break  # Break out of the loop if a valid odd number is entered
        except ValueError as e:
            print(e)  # Print the error message raised by ValueError
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except:
            print("Unexpected error occurred.")
            break

# Example usage:
get_odd_number()

