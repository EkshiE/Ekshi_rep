######   Задание 1   ######

# name = input('Ваше имя: ')
# years = int(input('Ваш возраст: '))
# if years > 18:
#     print(name + ', вы взрослый человек.')
# else:
#     print(name + ', вы ребенок.')

######   Задание 2   ######

while True:
    name = input('Ваше имя: ')
    years = int(input('Ваш возраст: '))
    if years > 18:
        print(name + ', вы взрослый человек.')
    else:
        print(name + ', вы ребенок.')
    if years == 0:
        break

######   Задание 3   ######

# import random    # модуль выбирает случайное число
# num = random.randint(1, 10)  # ф-ция определяет диапазон чисел от 1 до 10
# print('Я загадал число от 1 до 10.\nУгадай какое?\nУ тебя три попытки')
#
# for attempt in range(1, 4):  # 2-ой аргумент в ранге не включительно!
#     attempt = int(input('Введите число: '))
#     if attempt < num:
#         print('Неправильно. Моё число больше.')
#     elif attempt > num:
#         print('Неправильно. Моё число меньше.')
#     else:
#         break
# if attempt == num:
#     print('УРА!!! Ты победил!!!')
# else:
#     print('Извини, но победил я.\nПопробуй сыграть ещё раз.\nУ тебя всё получится! ')

###### ЗАДАНИЯ ДЛЯ ПРОДВИНУТЫХ ######

###    Задание 1   ###
# Мир Привет
# str_1, str_2 = 'Мир', 'Привет'
# print('!' + str_2, '!', str_1 + '!')
# print('!{a} ! {b}!'.format(a=str_2, b=str_1))
# print(f'!{str_2} ! {str_1}!')

###    Задание 2   ###

# name = input('Ваше имя: ')
# years = int(input('Ваш возраст: '))
#
# if years <= 0:
#     print('Ошибка, повторите ввод')   # не получилось со str
# elif(years < 10):
#     print(f'Привет, шкет {name}?')
# elif(years <= 18):
#     print(f'Как жизнь {name}?')
# elif(years < 100):
#     print(f'Что желаете, {name}?')
# else:
#     print(f'{name}, вы лжете- в наше время столько не живут...')

###   Задание 3   ###

while True:
    name = input('Ваше имя: ')
    years = int(input('Ваш возраст: '))

    if years <= 0:
        print('Ошибка, повторите ввод')   # не получилось со str
    elif years < 10:
        print(f'Привет, шкет {name}?')
    elif years <= 18:
        print(f'Как жизнь {name}?')
    elif years < 100:
        print(f'Что желаете, {name}?')
    else:
        print(f'{name}, вы лжете- в наше время столько не живут...')

###   Задание 4   ###

# 1 вариант с For:

# n = int(input('Введите число: '))
# b = 0
# c = 0
# for n in range(1, n+1):
#     b = (b + 1)
#     c = (c + (b ** 3))
# print(c)

#2 вариант с while:

n = int(input('Введите число: '))
b = 0
c = 0

while n:
    b = (b + 1)
    c = (c + (b ** 3))
    if b == n:
        break
print(c)
