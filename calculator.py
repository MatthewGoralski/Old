def calculator():
    while True:
        operation = input("Please enter an operation (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue

        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))

        if operation == '+':
            print("The result is: ", num1 + num2)
        elif operation == '-':
            print("The result is: ", num1 - num2)
        elif operation == '*':
            print("The result is: ", num1 * num2)
        else:
            if num2 == 0:
                print("Cannot divide by zero, please enter another number")
                continue
            print("The result is: ", num1 / num2)

        again = input("Do you want to continue? (yes/no) ")
        if again.lower() != 'yes':
            break

print("Welcome to the calculator!")
calculator()
print("Thank you for using our calculator!")