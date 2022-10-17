""" Homework for lesson 5  """

import timeit

""" Exercise 1 """


num_1 = lambda num=int(input('Введите число: ')): (print('Чётное')
                                                   if num % 2 == 0
                                                   else print('Нечётное')
                                                   )
num_1()


""" Exercise 2 """


print(list(map(lambda num: f'{num}', [1, 2, 3, 4, 5, 6, 7])))


""" Exercise 3 """
""" Choose polydromes """


print(
    tuple(filter(lambda tup: tup[::-1] == tup, ('доход', 'слово', 'шалаш',
                                                'сторона', 'заказ', 'список')))
)

""" Exercise 4 """


def my_dec(run_func):
    """ Print the execution time of two functions """

    def wrapper():
        start = timeit.default_timer()
        run_func()
        end = timeit.default_timer()
        print(f'seconds: {end - start}')

    return wrapper


@my_dec
def my_func():
    return tuple(filter(lambda tup: tup[::-1] == tup,
                        ('доход', 'слово', 'шалаш',
                         'сторона', 'заказ', 'список')))


my_func()


@my_dec
def get_gen():
    b = 1
    return [b * 2 for i in range(5)]


get_gen()
