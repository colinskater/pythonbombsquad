#defy the functions
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide (num1, num2):
    return num1 / num2

#take the input and variables
num1 = float(input("Enter a first number"))
num2 = float(input("Enter a second number"))
operation = (input("Enter a operation"))

#Write a algo 
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation")

#print the result
print("result: ", result)
