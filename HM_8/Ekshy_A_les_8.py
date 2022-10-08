""" Homework for lesson 8
Exercise 1: Creating a consumer class 'MyAuto
Exercise 2: Class heir 'Truck' and c lass heir 'Car'
:return: checking all methods and attributes
"""

from datetime import datetime
import time


class MyAuto:
    """
    Creating a consumer class
    :param brand: car brand
    :param age: year of car manufacture
    :param mark: car model
    :param color: car color
    :param weight: vehicle weight
    """
    brand = ''
    age = 0
    color = ''
    mark = ''
    weight = 3000

    def __init__(self, brand: str, age: int, mark: str):
        """ Method makes attributes required """

        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        """ Outputs the word 'move' when entering attributes """

        print('move')

    def birthday(self):
        """ Adds 1 to the year of manufacture of the car """

        print(self.age + 1)

    def stop(self):
        """ Outputs the word 'stop' when entering attributes """

        print('stop')


class Truck(MyAuto):
    """ Class heir 'MyAuto' """

    def __init__(self, brand: str, age: int, mark: str, max_load: int):
        """
        Adding a required attribute max_load
        :param max_load: Maximum vehicle load
        """

        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        """ Adds a word 'move' to a method 'attention' """

        print('attention')
        super().move()

    def load(self):
        """
        When calling the method, there is a pause of 1 second,
        then the message 'load' is issued and again a pause of 1 second
        """

        datetime.now(time.sleep(1))
        print('load')
        datetime.now(time.sleep(1))


class Car(MyAuto):
    """ Class heir 'MyAuto' """

    def __init__(self, brand: str, age: int, mark: str, max_speed: int):
        """
        Adding a required attribute max_speed
        :param max_speed: Maximum vehicle load
        """

        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        """ Displays the maximum vehicle load """

        super().move()
        print(f'max speed is {self.max_speed}')


my_auto = MyAuto('Audi', 2020, 'Q8')
my_auto.move()
my_auto.birthday()
my_auto.stop()

my_auto_1 = Truck('Audi', 2020, 'Q8', 3500)
my_auto_1.move()
my_auto_1.load()

my_auto_2 = Truck('Audi', 2020, 'Q8', 4000)
my_auto_2.move()
my_auto_2.load()

my_auto_4 = Car('Audi', 2020, 'Q8', 300)
my_auto_4.move()

my_auto_4 = Car('Audi', 2020, 'Q8', 290)
my_auto_4.move()
