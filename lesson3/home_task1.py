# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции

import random
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

# ищем сумму элементов списка, стоящих на нечётной позиции
def sum_of_odd_indices(input_list):
    summa = 0
    for i in range(1,len(input_list),2):
        summa = summa + input_list[i]
    return summa

# печатаем ресультат
def print_result(result):
    print(f'Сумма элементов стоящих на нечетных позициях = {result}')



num = input_data()
num_list = creating_list(num)
sum_of_odd_indices(num_list)
print_result(sum_of_odd_indices(num_list))


