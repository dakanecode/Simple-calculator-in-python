# simple calculator to perform operations such as addition, subtraction , muliplication and division



def calculator():
    # Get inputs from the user
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number:"))
    operation = input("Enter the operation( + , -, *, /): ")

    if operation == "+":
        print("The sum of num1 and num2 is ", num1+ num2)
    
    elif operation == "-":
         print("The diference of num1 and num2 is ", num1 - num2)
    elif operation == "*":
         print("The product of num1 and num2 is ", num1 * num2)
    elif operation == "/":
         print("The quotient of num1 and num2 is ", num1 / num2)

    else: 
         print("Invalid opearion")

calculator()