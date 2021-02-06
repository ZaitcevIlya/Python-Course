# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating_list = [7, 5, 3, 3, 2]

while True:
    new_rating = int(input('Enter your rating number: '))
    rating_list.append(new_rating)

    # Exit from infinite loop
    if new_rating == -1:
        break

    print(sorted(rating_list, reverse=True))
    print('\nIf you want to finish game enter -1 for exit\n')
