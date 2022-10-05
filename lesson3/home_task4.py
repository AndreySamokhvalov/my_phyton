# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное

import os
os.system("cls")
print('Добро пожаловать!')

# получение входных данных
def input_data():
    input_num = int(input("Введите десятичное число: "))
    os.system("cls")
    return input_num

# перевод в двоичную систему
def number_conversion(input_namber):
    binary = ''

    while input_namber > 0:
      binary = str(input_namber % 2) + binary
      input_namber = input_namber // 2
    return binary
# печать результата
def print_result(numb,result):
    print(f'Число {numb} в двоичной системе = {result}')


num = input_data()
number_conversion(num)
print_result(num,number_conversion(num))

