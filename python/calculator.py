def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:   #avoid the situation of division by zero
        return "Error: Division by zero is not allowed."
    
def calculator():
    print("Calculator")
    print("==========")
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:   # what does 'True' means here?
        choice = input("Enter choice (1/2/3/4):")

        if choice in ["1", "2", "3", "4" ]:    
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter the second number:"))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            print(f"Result:{result}\n")


        elif choice == "5":
            print("Thank you for using.")
            print("See you next time!")
            break
        else:
            print("Invalid input. Please try again.")


calculator()
