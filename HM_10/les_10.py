""" Homework for lesson 10"""


class Calculator:
    """ Class is a calculator. Work on the calculator in a while """
    number_1 = float
    number_2 = float
    my_operator = ['+', '-', '*', '/']

    def date(self):
        """
        Takes numeric values. If an invalid value is entered,
        it displays an error message.
        """
        try:
            self.number_1 = float(input('Enter the first number: '))
            self.number_2 = float(input('Enter the second number:'))
        except ValueError:
            print('Wrong numbers entered!')

    def math_symbol(self):
        """
        Mathematical symbol. If an invalid value is entered,
        it displays an error message.
        """

        self.my_operator = input('Action (+,-,*,/): ')
        if self.my_operator != ['+', '-', '*', '/']:
            print('Action entered incorrectly')

    def calculation(self):
        """
        Calculates the input and returns the result.
        Dividing by 0 throws an error
        """

        if self.my_operator == '+':
            print(self.number_1 + self.number_2)
        elif self.my_operator == '-':
            print(self.number_1 - self.number_2)
        elif self.my_operator == '*':
            print(self.number_1 * self.number_2)
        elif self.my_operator == '/':
            try:
                print(self.number_1 / self.number_2)
            except ZeroDivisionError:
                print('Cannot be divided by 0!')


c = Calculator()
while True:
    c.date()
    c.math_symbol()
    c.calculation()
