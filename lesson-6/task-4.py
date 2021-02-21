# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} started moving')
        pass

    def stop(self):
        print(f'{self.name} stopped')
        pass

    def turn(self, direction):
        print(f'{self.name} turned {direction}')
        pass

    def show_speed(self):
        print(f'{self.name} is moving with {self.speed} km/h')
        pass


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} is moving with {self.speed} is too fast for town. Slow down, please')
        else:
            print(f'{self.name} is moving with {self.speed} km/h')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} is moving with {self.speed} is too fast for working car. Slow down, please')
        else:
            print(f'{self.name} is moving with {self.speed} km/h')


class SportCar(Car):

    def show_speed(self):
        if self.speed < 100:
            print(f'{self.name} is moving with {self.speed} is too slow for this car type. Speed up!')
        else:
            print(f'{self.name} is moving with {self.speed} km/h')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


tc = TownCar(70, 'white', 'toyota', False)
print(tc.name)
tc.go()
tc.turn('left')
tc.show_speed()
tc.stop()

pc = PoliceCar(100, 'blue', 'cadillac')
print(pc.is_police)
pc.go()

sc = SportCar(90, 'yellow', 'porsche', False)
sc.show_speed()
sc.go()
sc.stop()

sc2 = SportCar(140, 'red', 'ferrari', True)
sc2.show_speed()
print(pc.is_police)

wc = WorkCar(35, 'grey', 'kamaz', False)
wc.go()
wc.show_speed()
wc.stop()

