# Написать программу получающую набор произведений чисел от 1 до N

import os
os.system("cls")
print('Добро пожаловать!')

# получение входных данных
def input_data():
    input_num = int(input("Введите значение N: "))
    os.system("cls")
    return input_num

# подсчет значений и заполнение списка
def calculete(number):
    result_list = []
    result = 1
    for i in range(1, number+1):
        result = result * i
        result_list.append(result)
    return result_list

# печать результата
def print_result(input_num, out_list):
    print(f'Набор произведений чисел от 1 до {input_num}: {out_list}')


num = input_data()
calculete(num)
print_result(num, calculete(num))
