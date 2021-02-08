# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_profile(name='John', surname='Smith', born='1979', city='New York', email='neo@theone.com', phone='555-55-55'):
    print(f'{name} {surname} {born} {city} {email} {phone}')


user_profile()
user_profile(name='Johnny', surname='Silverhand', born='1990',
             city='Nite City', email='dontcallmejohnny@da.com', phone='-')
