'''Odd Numbers
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?'''

for num in range(1,100):
  if num % 2 ==1:
    print(num)

#Bonus
for num in range(1,100,2):
  print(num)