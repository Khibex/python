# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

from random import randint


class Matrix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        res = ""
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                res += str(self.value[i][j]) + ' '
            res += '\n'
        return res

    def __add__(self, other):
        val = [[0 for _ in range(len(self.value))] for _ in range(len(self.value[0]))]
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                val[i][j] = self.value[i][j] + other.value[i][j]
        return Matrix(val)


matrix1 = Matrix([[randint(0, 10) for _i in range(0, 3)] for _ in range(0, 3)])
matrix2 = Matrix([[randint(0, 10) for _i in range(0, 3)] for _ in range(0, 3)])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
