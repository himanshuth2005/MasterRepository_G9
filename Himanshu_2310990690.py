print("Calculator to perform operation:")
print("Select a number to perform corresponding action:")
print("1 for multiplication, 2 for division, 3 for subtraction, 4 for exponent")

def multiplication(num1, num2):
    mul = num1 * num2
    print("Multiplication of the two numbers is:", mul)

def division(num1, num2):
    if num2 != 0:
        div = num1 / num2
        print("Division of the two numbers is:", div)
    else:
        print("Cannot divide by zero")

def subtraction(num1, num2):
    sub = num1 - num2
    print("Subtraction of the two numbers is:", sub)

def exponent(num1, num2):
    exp = num1 ** num2
    print("Exponentiation of the two numbers is:", exp)

Operation = int(input("Select the number from 1, 2, 3, 4: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if Operation == 1:
    multiplication(num1, num2)
elif Operation == 2:
    division(num1, num2)
elif Operation == 3:
    subtraction(num1, num2)
elif Operation == 4:
    exponent(num1, num2)
else:
    print("Invalid input. Please select a number from 1 to 4.")