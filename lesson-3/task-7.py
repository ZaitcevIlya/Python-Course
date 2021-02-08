# 7. Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().


def int_func(words):
    try:
        resulting_list = []

        for w in words.split(' '):
            resulting_list.append(w.title())

        return ' '.join(resulting_list)
    except TypeError:
        print('Wrong type. Only letters are available.')
    except AttributeError:
        print('Wrong type. Only letters are available')


print(int_func('hello'))
print(int_func('hello new world!!'))
print(int_func(1))