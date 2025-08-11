import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(x)

def calculator():
    print("Advanced Calculator")
    print("-------------------")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("0. Exit")

    while True:
        choice = input("\nEnter choice (0-7): ")
        if choice == '0':
            print("Exiting calculator. Goodbye!")
            break

        try:
            if choice in ['1', '2', '3', '4', '5']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                num = float(input("Enter number: "))
                print(f"Result: sqrt({num}) = {sqrt(num)}")
            elif choice == '7':
                num = int(input("Enter non-negative integer: "))
                print(f"Result: {num}! = {factorial(num)}")
            else:
                print("Invalid choice. Please select a valid operation.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()