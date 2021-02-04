# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и
# словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products_list = []
products_dict = {
    'name': [],
    'price': [],
    'quantity': [],
    'unit': set()
}

while True:
    product_id = len(products_list)

    while True:
        name = input('Enter product name: ')

        while True:
            try:
                price = int(input('Enter product price: '))
                break
            except ValueError:
                print('Error: This field cannot be empty. Enter only digits. Try again.')
        while True:
            try:
                quantity = int(input('Enter the quantity of products: '))
                break
            except ValueError:
                print('Error: This field cannot be empty. Enter only digits. Try again.')

        unit = input('Enter product unit: ')

        if (len(name) > 0) and (price != 0) and (quantity != 0) and len(unit) > 0:
            break
        else:
            print('Some of entered values are empty, pls enter again.')

    new_record = (product_id, {'name': name, 'price': price, 'quantity': quantity, 'unit': unit})
    products_list.append(new_record)

    products_dict['name'].append(name)
    products_dict['price'].append(price)
    products_dict['quantity'].append(quantity)
    products_dict['unit'].add(unit)

    print(f'\n{"#" * 15} Product tuples {"#" * 15}')
    for i in products_list:
        print(i, end='\n')

    print(f'\n{"#" * 15} Analytics {"#" * 15}')

    for k, v in products_dict.items():
        print(f'{k}: {v}')
