#####   Задание 1    ######

num_1 = 4
num_2 = 4
num_3 = 4
print(id(num_1))
print(id(num_2))
print(id(num_3))


#####   Задание 2    ######

# 1 вариант: ##

id_num_1 = 4
id_num_2 = 4
print(id(id_num_1))
print(id(id_num_2 + 1))

# 2 вариант: ##

num_3 = 4
num_4 = 4
print(id(num_3))
print(id('num_4'))


#####    Задание 3    ######

num_1 = 6
num_2 = 6
num_3 = 6
num_6 = 6
num_5 = 6

print(id(num_1))
print(id(float(num_2)))
print(id(str(num_3)))
print(id(num_6 + 1))
print(id(13 - num_5))

#####     Задание 4    ######

text = input("Введена строка: ")
text_1 = text[::2]
text_2 = text[1::2]
print('Введенная строка:' + text)
print()
print()
print(text_1 + ' ' + ' ' + ' ' + ' ' + ' ' + text_2 + '\n!!!')
