import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

lang = 'spanish'
continue_message = 'yes'

prompt(MESSAGES[lang]["welcome"])

while continue_message == 'yes':

    prompt(MESSAGES[lang]["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[lang]["invalid_number"])
        number1 = input()

    prompt(MESSAGES[lang]["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[lang]["invalid_number"])
        number2 = input()

    prompt(MESSAGES[lang]["operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES[lang]["invalid_operation"])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f'{MESSAGES[lang]["result"]}{output}')
    prompt(MESSAGES[lang]["continue"])
    continue_message = input()