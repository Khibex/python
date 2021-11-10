# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.im * other.re + self.re * other.im)

    def __str__(self):
        sign = '+ ' if self.im >= 0 else ''
        return f"{self.re} {sign}{self.im}i"


comp = Complex(2, 3)
comp1 = Complex(4, -10)
print(comp)
print(comp1)
comp2 = comp + comp1
print(comp2)
comp3 = comp * comp1
print(comp3)
