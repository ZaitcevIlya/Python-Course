# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

f_name = 'data-5.txt'
num_sequence = '4 5 6 3 2 33 29 77 82'


def calc_sum(data_str):
    str_to_list = data_str.split()
    return reduce((lambda x, y: x + y), [int(i) for i in str_to_list])


with open(f_name, 'w') as dest_f:
    dest_f.write(num_sequence)

with open(f_name, 'r') as src_f:
    data = src_f.read()
    print(calc_sum(data))
