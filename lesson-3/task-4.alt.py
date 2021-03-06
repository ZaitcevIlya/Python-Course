# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    if y == 0:
        return 1

    if y < 0 and type(y) != float:
        for i in range(y, -1, 1):
            x *= x

        return 1 / x
    else:
        print('Error. You entered wrong values. "Y" must be negative integer.')


print(my_func(5, -3))
print(my_func(5, -2))
print(my_func(4, -2))
print(my_func(4, -1))
