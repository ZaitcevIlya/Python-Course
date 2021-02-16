# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

f_name = 'data-3.txt'
formatted_employee_list = []


def find_small_salary(employee_list: list):
    salary_limiter = 20000
    employees = list(filter(lambda x: int(x[1]) < salary_limiter, employee_list))
    return [i[0] for i in employees]


def find_average_salary(employee_list: list):
    salary_only_list = [int(emp[1]) for emp in employee_list]
    numerator = reduce((lambda x, y: x + y), salary_only_list)
    denominator = len(employee_list)

    return round((numerator / denominator), 2)


try:
    with open(f_name, 'r') as my_f:
        list_of_employee = my_f.readlines()

        for i in list_of_employee:
            formatted_employee_list.append(i.split())

        print('These employees have less than 20.000 per year:')
        print('\n'.join(find_small_salary(formatted_employee_list)))

        print(f'\nAverage salary in company is {find_average_salary(formatted_employee_list)}')

except IOError:
    print('Some input-output error.')
