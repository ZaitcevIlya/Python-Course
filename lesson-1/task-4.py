# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# P.S. цикл for или например математические функции упростили бы код по пары строк

num = input('Enter integer: ')
num_len = len(num)
num_list = list(num)
max_char = num_list[0]

while num_len:
    new_max = num_list.pop()
    if max_char < new_max:
        max_char = new_max
    num_len -= 1

print(max_char)
