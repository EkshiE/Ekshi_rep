""" Homework for lesson 6  """
""" """
import csv
import json

""" Exercise 1 """

b_code = b'r\xc3\xa9sum\xc3\xa9'

decode_utf = b_code.decode()
print(decode_utf)

latin_code = decode_utf.encode('latin1')
print(latin_code)

code_str = latin_code.decode('latin1')
print(code_str)

""" Exercise 2 """

str_1 = 'JSON - текстовый формат обмена данных,'
str_2 = 'основанный на JavaScript. Но при этом формат'
str_3 = 'независим от JS и может использоваться в любом'
str_4 = 'языке программирования.'

file = open('text.txt', 'w')
file.write(f'{str_1}\n{str_2}')

file.close()

with open('text.txt', 'a') as file:
    file.write(f'\n{str_3}\n{str_4}')

""" Exercise 3 """

my_dict = {
    '222555': ['Vladimir', 35],
    '111333': ['Dmitry', 32],
    '333444': ['Sergei', 31],
    '555222': ['Yuri', 35],
    '666111': ['Alexei', 25],
    '888333': ['Nikolay', 37],
}

with open('my_dict.json', 'w') as file:
    json.dump(my_dict, file)


""" Exercise 4 """


with open('my_dict.json', 'r') as my_dict:
    my_dict = json.load(my_dict)

with open('cols.csv', 'w', encoding='utf-8') as file:
    cols = ['Id', 'Name', 'Age', 'Phone']
    csv_file = csv.DictWriter(
        file, delimiter=',',
        lineterminator='\r', fieldnames=cols
    )

    csv_file.writeheader()
    csv_file.writerow(
        {cols[0]: 222555,
         cols[1]: my_dict.get('222555')[0],
         cols[2]: my_dict.get('222555')[1],
         cols[3]: 375336667755}
    )

    csv_file.writerow(
        {cols[0]: 111333,
         cols[1]: my_dict.get('111333')[0],
         cols[2]: my_dict.get('111333')[1],
         cols[3]: 375336667755}
    )

    csv_file.writerow(
        {cols[0]: 333444,
         cols[1]: my_dict.get('333444')[0],
         cols[2]: my_dict.get('333444')[1],
         cols[3]: 375336643895}
    )

    csv_file.writerow(
        {cols[0]: 555222,
         cols[1]: my_dict.get('555222')[0],
         cols[2]: my_dict.get('555222')[1],
         cols[3]: 375446698575}
    )

    csv_file.writerow(
        {cols[0]: 666111,
         cols[1]: my_dict.get('666111')[0],
         cols[2]: my_dict.get('666111')[1],
         cols[3]: 375298842561}
    )

    csv_file.writerow(
        {cols[0]: 888333,
         cols[1]: my_dict.get('888333')[0],
         cols[2]: my_dict.get('888333')[1],
         cols[3]: 375297756435}
    )
