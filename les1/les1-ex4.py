# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num = input("Число: ")
i = 1
max_val = num[0]
while i < len(num):
    if max_val == 9:
        break
    if num[i] > max_val:
        max_val = num[i]
    i += 1
print(max_val)
