# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    str_date = ""

    def __init__(self, str):
        Date.str_date = str

    @classmethod
    def get_int(cls, param):
        day, month, year = Date.str_date.split('-')
        if param == 'd':
            return int(day)
        elif param == 'm':
            return int(month)
        elif param == 'y':
            return int(year)

    @staticmethod
    def valid(param):
        day, month, year = Date.str_date.split('-')
        if param == 'd':
            return 1 <= int(day) <= 31
        elif param == 'm':
            return 1 <= int(month) <= 12
        elif param == 'y':
            return 0 <= int(year) <= 3000

    def __str__(self):
        return Date.str_date


dt = Date("09-11-2021")
print(dt)

print(dt.get_int('d'))
print(dt.get_int('m'))
print(dt.get_int('y'))

dt1 = Date("29-13-2022")
print(dt1)

print(dt1.valid('d'))
print(dt1.valid('m'))
print(dt1.valid('y'))
