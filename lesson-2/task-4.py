# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

list_of_str = input('Enter a sentence of arbitrary length: ').split()

for ind, el in enumerate(list_of_str):
    print(ind, el if len(el) <= 10 else el[0:10])

