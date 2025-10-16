'''Build a program that displays when the user will retire and how many years she has to work till retirement.

Example
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!'''

from datetime import datetime

current_age = int(input('What is your age? '))
retirement_age = int(input('At what age would you like to retire? '))
years_to_retirement = retirement_age - current_age
CURRENT_YEAR = datetime.now().year

print(f'''It's {CURRENT_YEAR}.  You will retire in {CURRENT_YEAR + years_to_retirement}.
You have only {years_to_retirement} years of work to go!''')