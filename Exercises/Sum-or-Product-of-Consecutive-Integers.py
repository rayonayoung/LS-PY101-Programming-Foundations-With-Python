'''Sum or Product of Consecutive Integers
Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of
all numbers between 1 and the entered integer, inclusive.'''

number = int(input('Please enter an integer greater than 0: '))
choice = input('''Enter "s" to compute the sum, or "p" to compute the product. ''')
total = 1

if choice == 's':
    for num in range(2,number+1):
        total += num
    print(f'The sum of the integers between 1 and {number} is {total}')

elif choice == 'p':
    for num in range(1,number+1):
        total *= num
    print(f'The product of the integers between 1 and {number} is {total}')

