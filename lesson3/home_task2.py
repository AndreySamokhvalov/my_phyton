#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
import math
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_num = int(input("Укажите количество элементов в создаваемом списке: "))
    return input_num

# создание списка
def creating_list(imput_num):
    num_list = []
    for i in range(0, imput_num):
        num_list.append(random.randint(-100, 100))
    print(f'Сгенерированый список: {num_list}')
    return num_list

# ищем произведение пар чисел из списка
def the_product_of_pairs(imput_list):
    mod_list = []
    i = 0
    for i in range (0,math.ceil(len(imput_list)/2)):
        mod_list.append(imput_list[i]*imput_list[(i+1)*(-1)])
    return mod_list

# печать результата
def print_result(result_list):
    print(f'Произведение пар чисел сгенерированого списка: {result_list}')


num = input_data()
num_list = creating_list(num)
the_product_of_pairs(num_list)
print_result(the_product_of_pairs(num_list))
