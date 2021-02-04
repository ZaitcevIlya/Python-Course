# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Альтернативная версия с использованием словаря.

rating_dict = {
    '7': 1,
    '5': 1,
    '3': 2,
    '2': 1
}

while True:
    new_r_list = []
    new_value = input('Enter new rating value: ')

    if new_value == 'q':
        break

    if new_value in rating_dict.keys():
        rating_dict[new_value] += 1
    else:
        rating_dict[new_value] = 1

    for k, v in rating_dict.items():
        temp = [int(k)] * int(v)
        new_r_list.extend(temp)

    print(sorted(new_r_list, reverse=True))
