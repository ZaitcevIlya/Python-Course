# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и
# определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Enter the annual business proceeds: '))
costs = int(input('Enter the annual business costs: '))

financial_result = None
profitability = None

if proceeds > costs:
    financial_result = 'Profit'
    profitability = proceeds / (proceeds - costs)

    number_of_employees = int(input('How much employees work in your company? '))
    profit_per_employee = (proceeds - costs) / number_of_employees

    print(f'Your company annual result is {financial_result}.'
          f'\nProfitability is {profitability:.2f}.'
          f'\nProfit per employee is equal {profit_per_employee:.2f}.\nYou are doing well!')
elif proceeds == costs:
    print('You don`t get Loss but also don`t get Profit.\nCut the costs or modify your business model.')
else:
    financial_result = 'Loss'
    print(f'Your company annual result is {financial_result}.\nCut the costs!')
