
# +, -, /, *
# num_1 = int(input("Введите первое число: "))
# num_2 = input("Введите второе число: ")
# oper = input("+,-,*, /,: ")


number_1 = float(input("Введите первое число: "))
operation = input("Действие: ")
number_2 = float(input("Введите второе число: "))

if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("Делить на ноль нельзя!")
