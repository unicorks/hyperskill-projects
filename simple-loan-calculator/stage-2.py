principal = int(input("Enter the loan principal: "))
to_calc = input('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment''')

if to_calc == 'm':
    monthly_pay = int(input("Enter the monthly payment: "))
    m_monthly = -(-principal // monthly_pay)
    if m_monthly > 1:
        print(f'It will take {m_monthly} months to repay the loan')
    else:
        print(f'It will take {m_monthly} month to repay the loan')

elif to_calc == 'p':
    months = int(input("Enter the number of months: "))

    if principal % months == 0:
        print(f"Your monthly payment = {principal/months}")
    elif principal % months != 0:
        lastpayment = principal - (months - 1) * (-(-principal // months))
        print(f"Your monthly payment = {-(-principal // months)} and the last payment = {lastpayment}")
