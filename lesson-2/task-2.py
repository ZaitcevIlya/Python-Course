# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# Проверка на ввод чего угодно кроме последовательности цифр
while True:
    try:
        test_input = int(input('Enter a sequence of numbers: '))
        break
    except ValueError:
        print('Some of entered characters are not a number')

origin_list = list(str(test_input))
step = 2
i = 0

while i < len(origin_list):
    if i + step > len(origin_list):
        break
    else:
        origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        i = i + step

print(f'Sequence modified to {"".join(origin_list)}')
