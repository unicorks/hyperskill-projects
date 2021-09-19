import math

to_calc = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')

if to_calc == 'n':
    # take input
    principal = int(input('Enter the loan principal: '))
    annuity = float(input('Enter the monthly payment: '))
    interest = float(input('Enter the loan interest: '))
    interest = (1/12) * (interest/100)
    # calculation part
    payments = math.log(annuity / (annuity - interest * principal), interest + 1)
    payments = math.ceil(payments)
    # decide what to print
    if payments == 1:
        print('It will take 1 month to repay this loan!')
    elif payments < 12:
        print(f'It will take {payments} months to repay this loan!')
    else:
        years = payments // 12
        print(f'It will take {years} years and {payments % 12} months to repay this loan!')

if to_calc == 'a':
    # take input
    principal = int(input('Enter the loan principal: '))
    periods = int(input('Enter the number of periods:'))
    interest = float(input('Enter the loan interest: '))
    interest = (1 / 12) * (interest / 100)
    # calculation part
    annuity = math.ceil(principal * ((interest * pow(1 + interest, periods))/(pow(1 + interest, periods) - 1)))
    # print
    print(f'Your monthly payment = {annuity}!')

if to_calc == 'p':
    # take input
    annuity = float(input('Enter the annuity payment: '))
    periods = int(input('Enter the number of periods:'))
    interest = float(input('Enter the loan interest: '))
    interest = (1 / 12) * (interest / 100)
    # calculations
    principal = math.floor(annuity / ((interest * pow(1 + interest, periods))/(pow(1 + interest, periods) - 1)))
    # print
    print(f'Your loan principal = {principal}!')
