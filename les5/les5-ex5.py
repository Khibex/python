# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

st = input("Числа через пробел: ")
with open("les5-ex5.txt", 'w') as f_txt:
    print(st, file=f_txt)
with open("les5-ex5.txt") as f_txt:
    st = f_txt.readline()
total = 0
for num in st.split():
    total += float(num)
print(f"Сумма числе {total}")
