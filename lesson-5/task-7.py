# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

from functools import reduce
import json

src_f_name = 'data-7.txt'
report_f = 'financial-report.json'
firms_result = {}
firms_profit = []
financial_report = []


def make_financial_report(firm_data):
    for firm in firm_data:
        name = f'{firm[1]} {firm[0]}'

        proceeds = int(firm[2])
        costs = int(firm[3])

        financial_result = proceeds - costs

        firms_result[name] = financial_result

        if financial_result > 0:
            firms_profit.append(financial_result)

    financial_report.append(firms_result)
    average_profit = {'average_profit': round(reduce((lambda a, b: a + b), firms_profit) / len(firms_profit), 2)}
    financial_report.append(average_profit)


with open(src_f_name, 'r') as src_f:
    data = [i.split() for i in src_f.readlines()]
    make_financial_report(data)


with open(report_f, 'w') as dest_f:
    json.dump(financial_report, dest_f)
