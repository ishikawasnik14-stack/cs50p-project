def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculate(a, operator, b):
    """Perform a calculation based on the selected operator."""
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        raise ValueError("Invalid operator.")


def main():
    print("=================================")
    print("       PYTHON CALCULATOR")
    print("=================================")
    print("Enter 'q' at any time to quit.")
    print()

    while True:
        first = input("Enter first number: ")

        if first.lower() == "q":
            print("Goodbye!")
            break

        try:
            first = float(first)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        operator = input("Enter operator (+, -, *, /): ")

        if operator.lower() == "q":
            print("Goodbye!")
            break

        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Please choose +, -, * or /.\n")
            continue

        second = input("Enter second number: ")

        if second.lower() == "q":
            print("Goodbye!")
            break

        try:
            second = float(second)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        try:
            result = calculate(first, operator, second)
            print(f"Result: {result:g}")
        except ValueError as error:
            print(f"Error: {error}")

        print()


if __name__ == "__main__":
    main()