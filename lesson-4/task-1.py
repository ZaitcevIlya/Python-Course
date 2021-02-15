# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

_, p_output, p_rate, p_bonus = argv


def salary_calc(output, rate, bonus):
    try:
        output = int(output)
        rate = int(rate)
        bonus = int(bonus)
        return (output * rate) + bonus
    except ValueError:
        return 'Error. Some entered parameters are not an integer type.'


print(salary_calc(p_output, p_rate, p_bonus))
