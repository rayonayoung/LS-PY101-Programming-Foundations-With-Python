'''Isn't it Odd?
Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.'''

def is_it_odd(num):
  return abs(num) % 2 == 1

print(is_it_odd(3)) #True