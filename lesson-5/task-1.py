# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

f_name = 'data-1.txt'

try:
    open(f_name, 'x')
    print(f'File with name {f_name} was created. You can write your data.')
except FileExistsError:
    print('File already exists you can write something into.')

while True:
    input_data = input('Enter new message: ')

    if input_data == '':
        break

    try:
        with open(f_name, 'a') as my_f:
            my_f.write(f'{input_data}\n')
        print('Added')
    except IOError:
        print('Error. Some input-output error.')

    print('\nEnter an empty line for quit or ')
