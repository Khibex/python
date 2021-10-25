# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

total = 0
nr = 0
with open("les5-ex3.txt") as f_txt:
    print(f_txt.read())
    print()
    f_txt.seek(0)
    for line in f_txt:
        nr += 1
        last_name, salary = line.split()
        total += float(salary)
        if int(salary) < 20000:
            print(last_name, salary)
if nr != 0:
    print(f"Средний доход {total / nr}")
