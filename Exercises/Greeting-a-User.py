'''Write a program that asks for user's name, then greets the user. 
If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

Example1
What is your name? Sue
Hello Sue.

Example2
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?'''

def greet():
    user_name = input("What is your name? ")

    if '!' not in user_name:
        print(f'Hello {user_name}.')

    else:
        print(f'HELLO {user_name.upper()}! WHY ARE WE YELLING?')

greet()

#Alt: name.endswith("!")