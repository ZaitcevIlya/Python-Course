# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Enter the result of the first day (a): '))
b = int(input('Enter desired result (b): '))

days = 1
result_increment = 0.1

while a <= b:
    a = a + a * result_increment
    days += 1

print(f'Desired result will be reached on the {days} day.')
