# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing...')


class Pen(Stationery):

    def draw(self):
        print('Sorry, but pen is empty. Refill it!')


class Pencil(Stationery):

    def draw(self):
        print('You are drawing by pencil')


class Handle(Stationery):

    def draw(self):
        print('You are drawing by handle')


my_pen = Pen('coolest pen ever')
my_pen.draw()

my_pencil = Pencil('coolest pencil ever')
my_pencil.draw()

my_handle = Handle('coolest handle ever')
my_handle.draw()
