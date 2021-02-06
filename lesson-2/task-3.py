# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через List

while True:
    while True:
        try:
            month = int(input('Enter the number of any month (1-12): '))
            break
        except ValueError:
            print('Error: Some of entered characters are not a number. Try again.')

    months_list = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

    # Exit from infinite loop
    if month == 0:
        break

    if month in months_list[0]:
        print('This is winter month')
    elif month in months_list[1]:
        print('This is spring month')
    elif month in months_list[2]:
        print('This is summer month')
    elif month in months_list[3]:
        print('This is autumn month')
    else:
        print('You enter wrong number')

    print('\nIf you want to finish game enter 0 for exit\n')
