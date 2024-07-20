def calculator():
   
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /, %, **, b): ")

            if operation == "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operation == "*":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operation == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
            elif operation == "%":
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
            elif operation == "**":
                result = num1 ** num2
                print(f"{num1} ** {num2} = {result}")
            elif operation == "b":
                print(f"{num1} in binary: {bin(int(num1))[2:]}")
                print(f"{num2} in binary: {bin(int(num2))[2:]}")
            else:
                print("Invalid operation. Please try again.")

            another_calculation = input("Do you want to perform another calculation? (y/n): ")
            if another_calculation.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculator()