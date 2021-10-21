# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(num, den):
    if den == 0:
        return None
    else:
        return num / den


num1 = int(input("Числитель: "))
num2 = int(input("Знаменатель: "))
if num2 == 0:
    print("Деление на ноль")
else:
    print(division(num1, num2))
