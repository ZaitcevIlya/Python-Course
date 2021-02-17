# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

source_file = 'data-4.txt'
destination_file = 'data-4-mod.txt'

translation_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}
translated_list = []


def translator(f_list: list):
    """Split original data list to lowered string parts.
    Swap first element with translation reference from dictionary.
    Than back data to the initial format.
    """
    lower_and_split_l = [i.lower().split() for i in f_list]
    translated_split_l = []

    for i in lower_and_split_l:
        try:
            item = [translation_dict[i[0]], *lower_and_split_l[lower_and_split_l.index(i)][1:]]
            translated_split_l.append(item)
        except KeyError:
            print(f'Don`t have translation reference for word "{i[0]}". Update translation dictionary')

    return [' '.join(i).capitalize() for i in translated_split_l]


try:
    with open(source_file, 'r') as src_f:
        data = src_f.readlines()
        translated_list = translator(data)

    with open(destination_file, 'w') as dest_f:
        for line in translated_list:
            dest_f.write(f'{line}\n')

except IOError:
    print('Some input-output error.')
