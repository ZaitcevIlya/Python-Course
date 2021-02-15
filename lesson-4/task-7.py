# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.

def fact(num):
    factorial = 1

    if num < 0:
        print('Sorry, factorial exists only for positive numbers')
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial *= i
            yield factorial


n = 7
loop_id = 1

for el in fact(n):
    print(f'{loop_id}! = {el}')
    loop_id += 1
