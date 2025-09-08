print("Welcome to Calculator!")

#Ask the user for the first number
num1 = int(input("What is the first number?\n"))

#Ask the user for the second number
num2 = int(input("What is the second number?\n"))

operation = int(input('What operation would you like to perform? \n'))

if operation == 1:
    output = num1 + num2
elif operation == 2:
    output = num1 - num2
elif operation == 3:
    output = num1 * num2
elif operation == 4:
    output = num1 / num2
print(f'The result is: {output}')

#Testing development branch.



