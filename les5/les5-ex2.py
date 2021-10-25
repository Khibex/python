# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

str_nr = 0
word_nr = 0
with open("les5-ex1.txt") as f_txt:
    print(f_txt.read())
    f_txt.seek(0)
    for line in f_txt:
        str_nr += 1
        word_nr = len(line.split())
        print(f"Строка {str_nr} слов {word_nr}")
print(f"Всего строк {str_nr}")
