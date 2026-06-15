# Program to calculate the sum of two numbers with input validation

def read_number(prompt):
    """
    Safely read a number from the user.
    Retries until valid numeric input is received.
    """
    while True:
        try:
            value = input(prompt)
            # Try converting to float (supports integers and decimals)
            number = float(value)
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Read two valid numbers
    num1 = read_number("Enter first number: ")
    num2 = read_number("Enter second number: ")

    # Compute sum
    total = num1 + num2

    # Display result
    print("Sum of", num1, "and", num2, "is:", total)

if __name__ == "__main__":
    main()
