# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
from itertools import cycle


class TrafficLight:
    __color = ''
    __colors = cycle(['red', 'yellow', 'green', 'yellow'])

    def running(self):
        i = 0
        for color in self.__colors:
            self.__color = color

            if color == 'red':
                print(f'{self.__color} light - wait')
                time.sleep(7)
            elif color == 'green':
                print(f'{self.__color} light - go')
                time.sleep(5)
            else:
                print(f'{self.__color} light - wait')
                time.sleep(2)

            i += 1
            if i >= 10:
                break


my_light = TrafficLight()
my_light.running()

