import time


###### Задание 1-1 ######

# a = int(input('Введите число: '))
# a = [a for a in range(a + 1)]
# print(a)

###### Задание 1-2 ######

# def get_gen(b: str = str) -> list:
#     b = (input('Введите слово: '))
#     b = [b * 2 for i in range(5)]
#     print(b)
# get_gen()

###### Задание 1-3 ######

# Сначала поняла условие задания так:

# def get_num_with_time(
#         num_1: int = int, num_2: int = int
# ) -> int:
#     num_1 = int(input('Введите число: '))
#     num_1 = [num_1 for num_1 in range(num_1 + 1)]
#     print(num_1)
#     num_2 = int(input('Которое число извлечь из списка?: '))
#     num_2 = [num_1[num_2]]
#     from datetime import datetime
#     current_datetime = datetime.now().time()
#     print(num_2)
#     print(current_datetime)
# get_num_with_time()

# А потом решила, что правильно делать так:

# def get_date_time():
#     from datetime import datetime
#     date_time = [datetime.strftime(
#         datetime.now(), '%Y-%m-%d %H:%M:%S')]
#     print(date_time)
# get_date_time()

###### Задание 2-1 ######

# dict_1 = {'a': 1, 'b': 2}
# dict_2 = {}
# for key, val in dict_1.items():    # .items меняет местами ключи и значения
#     dict_2[val] = key
#     print(dict_2)

###### Задание 2-2 ######

# n = int(input('Введите число: '))
# b = 1
# c = 1
#
# while n:
#     b = (b + 1)
#     c = (c * b)
#     if b == n:
#         break
# print(c)

###### Задание 2-3 ######

# list_1 = input('Введите произвольный численный ряд: ')
# dict_1 = {}
# for num in list_1:
#     dict_1.setdefault(num, 0)  #метод .setdefault количество одинаковых values
#     dict_1[num] = dict_1[num] + 1
# print(dict_1)

###### Задание 2-4 ######

# def get_date_time():
#     b = int(input('Сколько раз повторить?: '))
#     from datetime import datetime
#     date_time = [datetime.strftime(datetime.now(time.sleep(1)), '%Y-%m-%d %H:%M:%S') for i in range(b)]
#     print(date_time)
#
# get_date_time()

