# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class Store:
    """
    Store implements the work of the warehouse.
    You can add office equipment to it and get information about capacity.
    Also it allows you to send equipment from store to some company departments.
    """

    store = {
        'printer': [],
        'scanner': [],
        'fax_machine': []
    }

    def add_to_store(self, prod_type, prod_obj):
        if self.store[prod_type]:
            if type(prod_obj) == list:
                self.store[prod_type].extend(prod_obj)
            else:
                self.store[prod_type].append(prod_obj)
        else:
            self.store[prod_type] = prod_obj if type(prod_obj) == list else [prod_obj]
        print(f'{prod_type} added to store')

    def get_prod_amount(self, prod_type):
        try:
            return len(self.store[prod_type])
        except KeyError:
            print(f'There is no such product: {prod_type} in store')

    def send_to_dept(self, department, prod_type, amount):
        prod_in_store = len(self.store[prod_type])

        if prod_in_store < amount:
            answer = input(f'You are trying to send {amount} {prod_type}s to some dept.\n'
                           f'At this moment we have only {prod_in_store}, send all of them? ')

            if answer == 'yes':
                self.send_to_dept(department, prod_type, prod_in_store)
            else:
                print(f'Ask your administrator for help')
        else:
            prods_for_sending = self.store[prod_type][:amount]

            if prod_type in Departments.departments[department]:
                Departments.departments[department][prod_type].extend(prods_for_sending)
            else:
                Departments.departments[department][prod_type] = prods_for_sending

            del self.store[prod_type][:amount]
            print(f'{amount} {prod_type}s sent to {department} dept')


class OfficeEquipment(ABC):

    is_on = False

    def __init__(self, prod_name, prod_type):
        self.prod_name = prod_name
        self.prod_type = prod_type

    def switch(self):
        self.is_on = not self.is_on
        print(f'This {self.prod_type} is turned {"on" if self.is_on else "off"}')

    @abstractmethod
    def get_status(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, prod_name, prod_type='printer', paper_capacity=50, color_capacity=100):
        self.color_capacity = color_capacity
        self.paper_capacity = paper_capacity
        super().__init__(prod_name, prod_type)

    def get_status(self):
        print(f'This {self.prod_type} have {self.paper_capacity} paper sheets and {self.color_capacity}% color')

    def do_print(self, doc):
        print(f'{self.prod_type} {self.prod_name} is printing {doc}')
        self.paper_capacity -= 1
        self.color_capacity -= 1


class Scanner(OfficeEquipment):

    def __init__(self, prod_name, prod_type='scanner'):
        super().__init__(prod_name, prod_type)

    def get_status(self):
        print(f'{self.prod_type} {"is ready to work" if self.is_on else "is turned off"}')

    def scan(self, doc):
        print(f'{self.prod_type} {self.prod_name} is scanning the {doc}')


class FaxMachine(OfficeEquipment):

    def __init__(self, prod_name, prod_type='fax_machine'):
        super().__init__(prod_name, prod_type)

    def get_status(self):
        print(f'{self.prod_type} {"is ready to work" if self.is_on else "is turned off"}')

    def do_call(self, phone):
        print(f'{self.prod_type} {self.prod_name} is calling to the {phone}')

    def do_print(self, doc):
        print(f'{self.prod_type} {self.prod_name} is printing {doc}')


class Departments:
    """
    Just a sample department class for testing transfer form store to some department
    """
    departments = {
        'financial': {},
        'tech': {},
        'HR': {}
    }


# Office Equipment functionality showing
p1 = Printer('Samsung', 'printer', 20, 60)
p1.switch()
p1.do_print('doc1.txt')
p1.get_status()
p2 = Printer('HP')
s1 = Scanner('Samsung')
s2 = Scanner('HP')
s3 = Scanner('Acer')
s4 = Scanner('Sony')
s1.switch()
s1.switch()
s1.scan('text1.txt')
f1 = FaxMachine('Samsung')
f1.get_status()
f1.switch()
f1.get_status()
f1.do_call('88005555555')

# Store functionality showing
print('\n')
s = Store()

# check for absent equipment
s.get_prod_amount('xerox')

# add item 1 by 1
s.add_to_store('printer', p1)
s.add_to_store('printer', p2)
print(f'Printers in the store: {s.get_prod_amount("printer")}')
[print(f'\t{i.prod_name}') for i in s.store['printer']]

# add list of items
s.add_to_store('scanner', [s1, s2, s3, s4])
print(f'Scanners in store: {s.get_prod_amount("scanner")}')
[print(f'\t{i.prod_name}') for i in s.store['scanner']]

# Departments functionality showing
print('\n')
d = Departments()
s.send_to_dept('financial', 'printer', 4)
if 'printer' in d.departments['financial']:
    print(f'Financial dept has printers:')
    [print(f'\t{i.prod_name}') for i in d.departments['financial']['printer']]
else:
    print(f'financial dept don`t have printers')

print(f'Printers in store: {s.get_prod_amount("printer")}')



