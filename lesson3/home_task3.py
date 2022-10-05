# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов

import random
import math
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_num = int(
        input("Укажите количество элементов в создаваемом списке: "))
    return input_num

# создание списка
def creating_list(imput_num):
    num_list = []
    for i in range(0, imput_num):
        num_list.append(round(random.uniform(0, 100), 4))
    print(f'Сгенерированый список: {num_list}')
    return num_list

# форматирование списка
def format_list(input_list):
    form_list = []
    for i in range(0, len(input_list)):
        form_list.append(round((input_list[i]-int(input_list[i])), 4))
    #print(form_list)
    return form_list

# поиск разницы между максимальной и минимальной дробной частью
def find_max_index(out_list):
    i = 0
    maxx = out_list[0]
    while i < len(out_list):
        if out_list[i] > maxx:
            maxx = out_list[i]
        i += 1

    j = 0
    minn = out_list[0]
    while j < len(out_list):
        if out_list[j] < minn:
            minn = out_list[j]
        j += 1
    result = maxx - minn
    return result

# печать результата
def print_result(out_num):
    print(f'Разница между максимальным и минимальным значением дробной части элементов: {out_num}')


num = input_data()
num_list = creating_list(num)
format_list(num_list)
find_max_index(format_list(num_list))
print_result(find_max_index(format_list(num_list)))
