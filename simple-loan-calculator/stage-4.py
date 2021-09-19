import sys
import argparse
import math

args = sys.argv
parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--interest")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--payment")

args = parser.parse_args()

# error cases
if args.type is None:
    print('Incorrect parameters.')
    exit()
if args.interest is None:
    print('Incorrect parameters.')
    exit()

t = [args.interest, args.principal, args.periods, args.payment]
t = list(filter(None, t))
if len(t) != 3:
    print('Incorrect parameters.')
t = [float(i) for i in t]
for m in t:
    if m < 0:
        print('Incorrect parameters.')
        exit()

if args.type == 'annuity':
    if args.periods is None:
        # define values from parameters
        principal = int(args.principal)
        annuity = float(args.payment)
        interest = float(args.interest)
        interest = (1 / 12) * (interest / 100)
        # calculation part
        payments = math.log(annuity / (annuity - interest * principal), interest + 1)
        payments = math.ceil(payments)
        # decide what to print
        if payments == 1:
            print('It will take 1 month to repay this loan!')
        elif payments < 12:
            print(f'It will take {payments} months to repay this loan!')
        elif payments % 12 == 0:
            print(f'It will take {payments//12} years to repay this loan!')
        else:
            years = payments // 12
            print(f'It will take {years} years and {payments % 12} months to repay this loan!')
        print(f'Overpayment = {math.ceil((annuity * payments) - principal)}')

    if args.payment is None:
        # take values
        principal = int(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)
        interest = (1 / 12) * (interest / 100)
        # calculation part
        annuity = math.ceil(principal * ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
        # print
        print(f'Your monthly payment = {annuity}!')
        print(f'Overpayment = {math.ceil((annuity * periods) - principal)}')

    if args.principal is None:
        # take input
        annuity = int(args.payment)
        periods = int(args.periods)
        interest = float(args.interest)
        interest = (1 / 12) * (interest / 100)
        # calculations
        principal = math.floor(annuity / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)))
        # print
        print(f'Your loan principal = {principal}!')
        print(f'Overpayment = {math.ceil((annuity * periods) - principal)}')

# differentiate payment
elif args.type == 'diff':
    n = 1
    principal = int(args.principal)
    periods = int(args.periods)
    interest = float(args.interest)
    interest = (1 / 12) * (interest / 100)
    total = 0

    while n <= periods:
        diff_pay = (principal/periods) + (interest * (principal - (principal * (n - 1)/periods)))
        print(f'Month {n}: payment is {math.ceil(diff_pay)}')
        total = total + math.ceil(diff_pay)
        n += 1

    print(f'\nOverpayment = {math.ceil(total - principal)}')
