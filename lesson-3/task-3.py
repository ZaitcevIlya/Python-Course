# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    l_args = [num_1, num_2, num_3]
    first_max = max(l_args)
    l_args.pop(l_args.index(first_max))
    second_max = max(l_args)
    return first_max + second_max


print(my_func(1, 2, 3))
print(my_func(19, 12, 3))
