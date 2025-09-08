def prompt(message):
    print(f'==> {message}')

def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    return False

prompt("Welcome to Calculator!")

#Ask the user for the first number
prompt("What is the first number?")
num1 = input()

while invalid_number(num1):
    prompt("Hmm...that doesn't look like a valid number.")
    num1 = input()

#Ask the user for the second number
prompt("What is the second number?")
num2 = input()

while invalid_number(num2):
    prompt("Hmm...that doesn't look like a valid number.")
    num2 = input()

operation = input('What operation would you like to perform? \n')

while operation not in ["1", "2", "3", '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()
    
match operation:
    case '1':
        output = int(num1) + int(num2)
    case '2':
        output = int(num1) - int(num2)
    case '3':
        output = int(num1) * int(num2)
    case '4':
        output = int(num1) / int(num2)

prompt(f'The result is: {output}')



