# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        temp = self.imaginary + other.imaginary
        if temp == 1:
            imaginary = '+ '
        elif temp == -1:
            imaginary = '- '
        else:
            imaginary = f'+ {temp}' if str(temp).find('-') == -1 else str(temp).replace('-', '- ')

        return f'{(self.real + other.real)} {imaginary}i'

    def __mul__(self, other):
        real_r = self.real * other.real - self.imaginary * other.imaginary
        imaginary_r = self.imaginary * other.real + self.real * other.imaginary
        imaginary_r = f'+ {imaginary_r}' if str(imaginary_r).find('-') == -1 else str(imaginary_r).replace('-', '- ')
        return f'{real_r} {imaginary_r}i'


cn1 = ComplexNumber(2, 5)
cn2 = ComplexNumber(3, -4)
cn3 = ComplexNumber(3, -6)
cn4 = ComplexNumber(4, 6)
print('add')
print(cn1 + cn2)
print(cn1 + cn3)
print(cn2 + cn3)
print(cn1 + cn4)
print('mul')
print(cn1 * cn2)
print(cn1 * cn3)
print(cn2 * cn3)
print(cn1 * cn4)
