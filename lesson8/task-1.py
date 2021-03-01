# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    """
    input: string formatted as 'day-month-year'
    """

    def __init__(self, date: str):
        setattr(Date, 'date', date)

    @classmethod
    def date_to_int(cls):
        date = list(map(int, cls.__dict__['date'].split('-')))
        day = cls.validate(date[0], 'day')
        month = cls.validate(date[1], 'month')
        year = cls.validate(date[2], 'year')
        print(day, month, year)

    @staticmethod
    def validate(num, num_type):
        if num_type == 'day':
            if 31 >= num > 0:
                return num
            else:
                raise ValueError(num_type, num)
        elif num_type == 'month':
            if 12 >= num > 0:
                return num
            else:
                raise ValueError(num_type, num)
        elif num_type == 'year':
            if num > 0:
                return num
            else:
                raise ValueError(num_type, num)


try:
    d1 = Date('23-04-1990')
    Date.date_to_int()
    d2 = Date('23-06-1992')
    d2.date_to_int()
    d3 = Date('54-04-1992')
    d3.date_to_int()
except ValueError as inst:
    num_type, num = inst.args
    print(f'You entered {num_type} = {num}')
    print('The day can be only integer in range 1 - 31.\n'
          'The month can be only integer in range 1 - 12.\n'
          'The year must be a positive integer')
