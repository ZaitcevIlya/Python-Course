# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def iter_a(start):
    try:
        start = int(start)
    except ValueError:
        print('Error. Entered value is not an integer.')
        return

    for el in count(start):
        if el > 10:
            break
        print(el)


def iter_b(s_list):
    steps = 0

    for el in cycle(s_list):
        if steps > 10:
            break
        print(el)
        steps += 1


some_list = ['hello', 'new', 'world']

iter_a(5)
iter_b(some_list)
