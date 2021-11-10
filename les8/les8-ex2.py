# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num1 = int(input("Числитель: "))
    num2 = int(input("Знаменатель: "))
    if num2 == 0:
        raise ZeroException("Деление на 0!")
    print(num1 / num2)
except ZeroException as e:
    print(e)
