'''Write two different ways to remove all of the elements 
from the following list:

numbers = [1, 2, 3, 4]
'''
numbers = [1, 2, 3, 4]

#Method 1: clear()

numbers.clear()

#Method 2: del()

del numbers[0:len(numbers)]

#Method 3: pop()

while numbers:
    numbers.pop()