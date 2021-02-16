# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

import re
from functools import reduce

f_name = 'data-6.txt'
subj_by_hours = {}

with open(f_name, 'r') as src_f:
    data = src_f.readlines()

    for line in data:
        end_of_subj_str = line.find(':')
        subject = line[0:end_of_subj_str]

        nums_from_str = re.findall(r'\d+', line)
        total_hours = int(reduce((lambda x, y: int(x) + int(y)), nums_from_str))

        subj_by_hours[subject] = total_hours

print(subj_by_hours)
