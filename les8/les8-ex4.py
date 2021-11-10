# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Store:
    def __init__(self, name):
        self.name = name


class Equipment:
    def __init__(self, name):
        self.name = name


class Printer(Equipment):
    def __init__(self, name, speed):
        super(name)
        self.speed = speed


class Scanner(Equipment):
    def __init__(self, name, dpi):
        super(name)
        self.dpi


class Xerox(Equipment):
    def __init__(self, name, list_format):
        super(name)
        self.list_format = list_format
