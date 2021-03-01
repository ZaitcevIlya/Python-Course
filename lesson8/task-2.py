# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    nums = input('This is division app. Enter two number separated by space: ')
    nums = list(map(int, nums.split(' ')))

    if nums[1] == 0:
        raise MyZeroDivision('You are not allowed to divide by zero.')
    else:
        print(round(nums[0] / nums[1], 2))
except MyZeroDivision as err_obj:
    print(err_obj.txt)