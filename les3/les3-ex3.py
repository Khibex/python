# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def sum_two_max(num1, num2, num3):
    min_num = sum_val = num1
    for n in (num2, num3):
        min_num = n if n < min_num else min_num
        sum_val += n
    return sum_val - min_num


n1 = int(input("Первое число: "))
n2 = int(input("Второе число: "))
n3 = int(input("Третье число: "))
print(sum_two_max(n1, n2, n3))
