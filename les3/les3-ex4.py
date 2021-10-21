# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func(x, y):
    return x ** y


def my_func1(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return 1 / res


n1 = int(input("Положительное число: "))
n2 = int(input("Отрицательное целое число: "))
print(my_func(n1, n2))
print(my_func1(n1, n2))
