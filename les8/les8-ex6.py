# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class WordException(Exception):
    def __init__(self, txt):
        self.txt = txt


class BaseObject:
    @classmethod
    def valid_num(cls, num):
        res = False
        try:
            for ch in num:
                if not ch.isdigit():
                    raise WordException("Не цифровой символ")
            res = True
        except WordException as e:
            print(e)
        finally:
            return res


class Store(BaseObject):
    def __init__(self, name):
        self.name = name
        self.list = []

    def add(self, equipment, num):
        for i in range(num):
            self.list.append(equipment)

    def to_department(self, cls, department, num):
        equipment = None
        for i in range(num):
            equipment = list(filter(lambda p: type(p) is cls, self.list))[0]
            self.list.remove(equipment)
        department.add(equipment, num)

    def get_nr(self):
        print(f"Оборудования на складе {len(self.list)}")
        return len(self.list)

    def get_equipment_nr(self, cls):
        print(f"{cls.prn()} на складе {sum(map(lambda p: type(p) is cls, self.list))}")
        return sum(map(lambda p: type(p) is cls, self.list))


class Department(Store):
    def get_nr(self):
        print(f"Оборудования в подразделении {len(self.list)}")
        return len(self.list)

    def get_equipment_nr(self, cls):
        print(f"{cls.prn()} в подразделении {sum(map(lambda p: type(p) is cls, self.list))}")
        return sum(map(lambda p: type(p) is cls, self.list))


class Equipment(BaseObject):
    def __init__(self, name):
        self.name = name


class Printer(Equipment):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    @classmethod
    def prn(cls):
        return "Принтер"


class Scanner(Equipment):
    def __init__(self, name, dpi):
        super().__init__(name)
        self.dpi = dpi

    @classmethod
    def prn(cls):
        return "Сканер"


class Xerox(Equipment):
    def __init__(self, name, list_format):
        super().__init__(name)
        self.list_format = list_format

    @classmethod
    def prn(cls):
        return "Копир"


store = Store(1)
while True:
    st = input("Завезли принтеров на склад, название скорость количество: ")
    nm, param, nr = st.split()
    if Printer.valid_num(nr) and Printer.valid_num(param):
        store.add(Printer(nm, int(param)), int(nr))
        break

while True:
    st = input("Завезли сканеров на склад, название разрешение количество: ")
    nm, param, nr = st.split()
    if Scanner.valid_num(nr) and Scanner.valid_num(param):
        store.add(Scanner(nm, int(param)), int(nr))
        break

while True:
    st = input("Завезли копиров на склад, название лист количество: ")
    nm, param, nr = st.split()
    if Xerox.valid_num(nr):
        store.add(Xerox(nm, param), int(nr))
        break

store.get_nr()
store.get_equipment_nr(Printer)
store.get_equipment_nr(Scanner)
store.get_equipment_nr(Xerox)

dep = Department("d1")
while True:
    nr = input("Передать принтеры со склада в подразделение, количество: ")
    if Printer.valid_num(nr):
        store.to_department(Printer, dep, int(nr))
        print(f"Передали принтеры в подразделение {nr}")
        break

while True:
    nr = input("Передать сканеры со склада в подразделение, количество: ")
    if Scanner.valid_num(nr):
        store.to_department(Scanner, dep, int(nr))
        print(f"Передали сканеры в подразделение {nr}")
        break

while True:
    nr = input("Передать копиры со склада в подразделение, количество: ")
    if Printer.valid_num(nr):
        store.to_department(Xerox, dep, int(nr))
        print(f"Передали копиры в подразделение {nr}")
        break

store.get_nr()
store.get_equipment_nr(Printer)
store.get_equipment_nr(Scanner)
store.get_equipment_nr(Xerox)
dep.get_nr()
dep.get_equipment_nr(Printer)
dep.get_equipment_nr(Scanner)
dep.get_equipment_nr(Xerox)
