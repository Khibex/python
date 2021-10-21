# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
def int_func(txt):
    return txt[0].upper() + txt[1:]


s = input("Слово: ")
print(int_func(s))
