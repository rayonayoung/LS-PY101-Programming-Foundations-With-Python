'''Tip Calculator
Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip,
then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.'''

bill_amount = float(input('What is the bill? '))
tip_percentage = float(input('What is the tip percentage? '))
tip_amount = bill_amount * tip_percentage/100
total = bill_amount + tip_amount

print(f'\nThe tip is ${tip_amount:.2f}.\nThe total is ${total:.2f}')