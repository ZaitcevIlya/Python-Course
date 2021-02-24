# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    """
    The class implement overloading methods for arithmetic operators: +, -, *, \
    All of them can be applied to class instances.
    """
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result < 0:
            return Cell('Error. Subtraction only works for positive result.')
        return Cell(result)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        try:
            result = self.quantity // other.quantity
            return Cell(result)
        except ZeroDivisionError:
            return Cell('Error. Division by zero')

    def make_order(self, item_per_row):
        string = '*' * self.quantity
        result = '\n'.join([string[i:i + item_per_row] for i in range(0, len(string), item_per_row)])
        print(result)


c1 = Cell(12)
c2 = Cell(15)
c3 = Cell(0)
r1 = c1 - c2
r2 = c2 - c1
r3 = c1 * c2
r4 = c2 / c1
r5 = c2 / c3
print(r1.quantity)
print(f'New Cell with quantity = {r2.quantity}')
print(f'New Cell with quantity = {r3.quantity}')
print(f'New Cell with quantity = {r4.quantity}')
print(f'New Cell with quantity = {r5.quantity}')
print(f'Cell {c1.quantity}:')
c1.make_order(5)
print(f'Cell {c2.quantity}:')
c2.make_order(5)

