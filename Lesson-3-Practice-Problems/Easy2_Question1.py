'''Write two distinct ways of reversing the list without 
mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
'''
numbers = [1, 2, 3, 4, 5]    

#Method 1: Slicing

print(numbers[::-1])

#Method 2: Reversed()

print(list(reversed(numbers)))




