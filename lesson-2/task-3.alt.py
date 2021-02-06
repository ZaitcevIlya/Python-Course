# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через Dict

while True:
    while True:
        try:
            month = int(input('Enter the number of any month (1-12): '))
            break
        except ValueError:
            print('Error: Some of entered characters are not a number. Try again.')

    # Exit from infinite loop
    if month == 0:
        break

    month_dict = {
        'winter': (12, 1, 2),
        'spring': (3, 4, 5),
        'summer': (6, 7, 8),
        'autumn': (9, 10, 11)
    }

    for key, value in month_dict.items():
        if month in value:
            print(f'This is {key} month')

    print('\nIf you want to finish game enter 0 for exit\n')
