""" This module converts Fahrenheit to Kelvin """

from prettytable import PrettyTable


def kelvin(fahrenheit: int) -> str:
    """
    Converts temperature from Fahrenheit to Kelvin
    :param fahrenheit: Value in degrees Fahrenheit
    :return: Text table
    """
    kelvin_value = 5. / 9. * (fahrenheit - 32) + 273.15
    table = PrettyTable(['Фаренгейты', 'Кельвины'])
    table.add_row([fahrenheit, kelvin_value])

    return table.get_string()



