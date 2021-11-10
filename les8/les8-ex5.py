# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

class Store:
    def __init__(self, name):
        self.name = name
        self.list = []

    def add(self, equipment, num):
        for i in range(num):
            self.list.append(equipment)

    def to_department(self, equipment, department, num):
        for i in range(num):
            self.list.remove(equipment)
        department.add(equipment, num)

    @property
    def get_nr(self):
        return len(self.list)

    def get_equipment_nr(self, cls):
        return sum(map(lambda p: type(p) is cls, self.list))


class Equipment:
    def __init__(self, name):
        self.name = name


class Printer(Equipment):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed


class Scanner(Equipment):
    def __init__(self, name, dpi):
        super().__init__(name)
        self.dpi = dpi


class Xerox(Equipment):
    def __init__(self, name, list_format):
        super().__init__(name)
        self.list_format = list_format


store = Store(1)
printer = Printer("p1", 100)
store.add(printer, 10)
scanner = Scanner("s1", 600)
store.add(scanner, 3)
xerox = Xerox("x1", "A4")
store.add(xerox, 5)
print(f"Оборудования на складе {store.get_nr}")
print(f"Принтеров на складе {store.get_equipment_nr(Printer)}")
print(f"Сканеров на складе {store.get_equipment_nr(Scanner)}")
print(f"Копиров на складе {store.get_equipment_nr(Xerox)}")

# Так как склад это тоже подразделение, для упрощения примем подразделение тип Store

dep = Store("d1")
store.to_department(printer, dep, 2)
print("Передали принтеры в подразделение")
store.to_department(xerox, dep, 1)
print("Передали копиры в подразделение")
print(f"Оборудования на складе {store.get_nr}")
print(f"Принтеров на складе {store.get_equipment_nr(Printer)}")
print(f"Копиров на складе {store.get_equipment_nr(Xerox)}")
print(f"Оборудования в подразделении {dep.get_nr}")
print(f"Принтеров в подразделении {dep.get_equipment_nr(Printer)}")
print(f"Копиров в подразделении {dep.get_equipment_nr(Xerox)}")
