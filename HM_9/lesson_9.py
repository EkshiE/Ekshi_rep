"""
Homework for lesson 9
Exercise 1: Make your own data class
:param title_flower: Flower name
:param amount: Quantity in stock
:param storage: Warehouse storage
:return: Printing flower name, stock quantity and storage number

Exercise 2: Add a static method to the class
:return: String output

Exercise 3: Add a class method to the class
:return: Overriding Attributes

Exercise 4: Create metaclass
Creating a metaclass 'House' based on the parent class 'Building'
"""

from dataclasses import dataclass


@dataclass
class Flower:
    title_flower: str
    amount: int
    storage: int

    @staticmethod
    def beginning_of_work():
        """ String output  """
        print(f'Good morning!')

    @classmethod
    def __init__(cls, title_flower, amount, storage):
        cls.title_flower = title_flower
        cls.amount = amount
        cls.storage = storage

    def get_flower(self):
        """ Redefining and Formatting Attributes """
        print(f'{self.title_flower}: {self.amount}, {self.storage}')


flower = Flower('lily', 100, 5)
print(flower)

flower.beginning_of_work()

flower.__init__('orchid', 30, 2)
flower.get_flower()


class Building:
    buildings = {'1': 5, '2': 7, '3': 7, '4': 8, '5': 3, '6': 12}
    num_building = int

    def data(self):
        """
        Entering the house number. Displaying the
        umber of floors by house number
        """

        self.num_building = input('Enter house number (1-6): ')

        print(
            f'Num building: {self.num_building}, '
            f'floors: {self.buildings.get(self.num_building)}'
        )


class House(metaclass=type):

    def __str__(self):
        """ String output """
        self.location = 'In the city'
        print(self.location)


building = Building()
building.data()

house = House()
house.__str__()
