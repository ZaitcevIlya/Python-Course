# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

while True:
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))


    def divider(a, b):
        return round((a / b), 2)

    try:
        print(divider(num_1, num_2))
        print('Type ctrl+z for exit\n')
    except ZeroDivisionError as err:
        print('Error. You can`t divide by zero')

