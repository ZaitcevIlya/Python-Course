# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_formatted = ''
        for i in self.matrix:
            for j in i:
                matrix_formatted += f'{j}\t'
            matrix_formatted += '\n'
        return matrix_formatted

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            result = [list(map(sum, zip(*t))) for t in zip(self.matrix, other.matrix)]
            return Matrix(result)
        else:
            return f'Error. Two matrices must have an equal number of rows and columns to be added.'


m = Matrix([[31, 22], [37, 43], [51, 86]])
print('Matrix formatted')
print(m)
print('Sum of two matrix')
print(m + m)

m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print('Matrix formatted')
print(m2)
print('Sum of two matrix with different length of row or column')
print(m + m2)

