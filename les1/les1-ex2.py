# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input("Секунды: "))
print("%02d:%02d:%02d" % (sec // 3600, (sec % 3600) // 60, (sec % 3600) % 60))
