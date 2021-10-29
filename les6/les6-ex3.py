# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_ful_name(self):
        return self.surname + " " + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


ivanov = Position("Иван", "Иванов", "Специалист", 20000, 1000)
print(ivanov.name, ivanov.surname, ivanov.position)
print(ivanov.get_ful_name())
print(f"Доход {ivanov.get_total_income()} руб\n")

petrov = Position("Петр", "Петров", "Эксперт", 30000, 3000)
print(petrov.name, petrov.surname, petrov.position)
print(petrov.get_ful_name())
print(f"Доход {petrov.get_total_income()} руб")
