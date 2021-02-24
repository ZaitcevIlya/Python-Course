# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    overall_fabric_consumption = 0

    def __init__(self, cl_type):
        super().__init__()
        self.cl_type = cl_type

    @abstractmethod
    def fabric_consumption_calc(self):
        pass


class Coat(Clothes):

    def __init__(self, cl_type, size):
        super().__init__(cl_type)
        self.size = size

    def fabric_consumption_calc(self):
        result = round(self.size / 6.5 + 0.5, 2)
        Clothes.overall_fabric_consumption += result
        return result


class Suit(Clothes):

    def __init__(self, cl_type, height):
        super().__init__(cl_type)
        self.height = height

    def fabric_consumption_calc(self):
        result = round(2 * self.height + 0.3, 2)
        Clothes.overall_fabric_consumption += result
        return result


cl1 = Coat('coat', 50)
fabric_amount_1 = cl1.fabric_consumption_calc()
print(f'Fabric consumption for {cl1.cl_type} - {fabric_amount_1}')
print(f'Overall fabric consumption: {Clothes.overall_fabric_consumption}')

cl2 = Suit('suit', 1.8)
fabric_amount_2 = cl2.fabric_consumption_calc()
print(f'Fabric consumption for {cl2.cl_type} - {fabric_amount_2}')
print(f'Overall fabric consumption: {Clothes.overall_fabric_consumption}')

cl3 = Coat('coat', 34)
fabric_amount_3 = cl3.fabric_consumption_calc()
print(f'Fabric consumption for {cl3.cl_type} - {fabric_amount_3}')
print(f'Overall fabric consumption: {Clothes.overall_fabric_consumption}')
