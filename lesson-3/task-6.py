# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(word):
    try:
        return word.title()
    except TypeError:
        print('Wrong type. Only letters are available.')
    except AttributeError:
        print('Wrong type. Only letters are available')


print(int_func('text'))
print(int_func(1))