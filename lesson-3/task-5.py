# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# I store the initialization data in a dictionary so I can cache the result and
# use it to reduce the looping passes below.
data = {
    'numbers': [],
    'result': 0,
    'continue_calculation': True
}


def my_calc():
    """Ask to input sequence of numbers and calculate the sum of all numbers. Then ask to enter another one.

    It run through whole list only if data[result] is 0,
    else it just run through new added values and sum them to previous calculation which stored in data[result]
    """
    str_numbers = input('Enter a sequence of numbers divided by space: ')
    added_numbers = str_numbers.split(' ')
    data['numbers'].extend(str_numbers.split(' '))

    for i in data['numbers'] if data['result'] == 0 else added_numbers:
        try:
            i_to_int = int(i)
            data['result'] += i_to_int
        except ValueError:
            print(f'You entered some non integer value. Current result is {data["result"]}')
            return False

    return print(data['result'])


while data['continue_calculation']:
    total = my_calc()
    if type(total) == bool:
        continue_calculation = total
    else:
        total
