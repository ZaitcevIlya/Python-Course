# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

type_list = [123, 3.14, 3+5j, 'data', {'a': 1, 'b': 2}, (1, 2), [1, 2], True]

for i in type_list:
    print(f'Item {i} is of {type(i)} type')
