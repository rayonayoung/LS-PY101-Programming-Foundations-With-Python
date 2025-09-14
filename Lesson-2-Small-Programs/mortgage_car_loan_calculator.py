print('Welcome to Car Loan Calculator!')

def get_float(prompt):
    while True:
        num = input(prompt)
        try:
            float(num)
            break
        except ValueError:
            print('You must enter a number.')
    return float(str)

while True:
    loan_amount = get_float('Enter loan amount: ')
    apr = get_float('Enter Annual Percentage Rate: ')
    loan_duration_years = get_float('Enter Loan Duration (years): ')
    monthly_interest_rate = apr/100/12
    loan_duration_months = loan_duration_years * 12
    try:
        monthly_payment = (
            loan_amount
            * (
                monthly_interest_rate
                / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months))
            )
        )
        print(f'Your monthly payment is {monthly_payment}')
        break

    except ZeroDivisionError:
        print('Cannot divide by zero. Try again.')
