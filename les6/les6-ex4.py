# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = None

    def go(self, speed):
        self.speed = speed
        print("Поехали")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print("Остановились")

    def turn(self, direction):
        self.direction = direction
        print(f"Повернули {self.direction}")

    def show_speed(self):
        print(f"Скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed < 60:
            print("Низкая скорость!")


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.speed}")
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


town = TownCar("Серый", "Такси")
print(f"Название: {town.name}\nЦвет: {town.color}\nПолицейский? {town.is_police} ")
town.go(70)
town.speed = 60
town.show_speed()
town.turn("Направо")

work = WorkCar("Белый", "Джип")
print(f"\nНазвание: {work.name}\nЦвет: {work.color}\nПолицейский? {work.is_police} ")
work.go(40)
work.turn("Налево")
work.stop()

police = PoliceCar("Черный", "Патруль")
print(f"\nНазвание: {police.name}\nЦвет: {police.color}\nПолицейский? {police.is_police} ")
police.go(80)

sport = SportCar("Красный", "МиГ")
print(f"\nНазвание: {sport.name}\nЦвет: {sport.color}\nПолицейский? {sport.is_police} ")
sport.go(50)
