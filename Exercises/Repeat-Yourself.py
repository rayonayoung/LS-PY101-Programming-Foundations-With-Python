'''Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

Example
repeat('Hello', 3)'''

def repeat(string, int):
    for idx in range(int):
        print(string)

repeat('Hello', 3)
