# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def person(first_name, last_name, year, city, email, tel):
    print(first_name, last_name, year, city, email, tel)


n = input("Имя: ")
ln = input("Фамилия: ")
y = input("Год рождения: ")
c = input("Город проживания: ")
e = input("Email: ")
t = input("Телефон: ")
person(first_name=n, last_name=ln, year=y, city=c, email=e, tel=t)
