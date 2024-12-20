# Prompting the user for the input of the two numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

# Prompting the user for the operation to be performed
operation = input("Choose the operation (+, -, *, /):").stript()

match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition}")
    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}")
    case "*":
        multiplication = num1 * num2
        print(f"The result is {multiplication}")
    case "/":
        division = num1 / num2
        print(f"The result is {division}")
    case _:
        print("Invalid operation. Please choose from +, -, *, /")

