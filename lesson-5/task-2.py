# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f_name = 'data-2.txt'

try:
    with open(f_name, 'r') as my_f:
        list_lines = my_f.readlines()
        lines_amount = len(list_lines)

        if lines_amount == 0:
            print(f'File "{f_name}" is empty')
        else:
            print(f'File "{f_name}" has {lines_amount} line{"" if lines_amount == 1 else "s"}')

            for num, chars in enumerate(map(len, list_lines), start=1):
                print(f'Line {num} contains {chars} characters')

except IOError:
    print('Some input-output error')