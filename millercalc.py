from fractions import Fraction

# this function will add two numbers together
def add(num1, num2):
    return num1 + num2

# this function will substract two numbers from each other
def subtract(num1, num2):
    return num2 - num1

# this function will multiply two numbers togethers
def multiply(num1, num2):
    return num1 * num2

# this function will divide two numbers 
def divide(num1, num2):
    return num1 / num2

# This next section is asking the user if they wanet to add, substract, multiply, or divide 
print("Select operation for your equation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# This next section will prompt the user to provide the information needed to preform the calculations
while True:
    # Prompting the user for the operation needed for the calculation
    operation = input("Enter operation 1, 2, 3, or 4: ")

    # Read the user input from the user and preform the mathematics to give the user to the user. 
    if operation in ('1', '2', '3', '4'):
        try: 
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number:"))
        except ValueError:
            print("Invaild input. Please enter a number")
            continue

        if operation == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        elif operation == '2':
            print(num2, "-", num1, "=", subtract(num1,num2))
        elif operation == '3':
            print(num1, "x", num2, "=", multiply(num1,num2))
        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # Next I will see if the user wants preform another calculation
        next_calculation = input("Would you like to preform another calculation: ")
        if next_calculation == "no":
            break
        else:
            print("Invalid Input") 
