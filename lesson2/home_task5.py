#Реализовать алгоритм перемешивания списка

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
        num_list.append(random.randint(1, 100))
    print(num_list)
    return num_list

# перемешивание списка
def mixing_list(imput_list):
    out_list = []
    i = 0
    while i < len(imput_list):
        out_list.append(imput_list[i])
        i+=1
    random.shuffle(out_list)
    print(out_list)
    return out_list

# печать 
def print_list(origin_list, mix_list):
    print(f' Сгенерированый список: {origin_list} ')
    print(f' Список после перемешивания: {mix_list}')
   
num = input_data()
num_list = creating_list(num)
mix_num_list = mixing_list(num_list)
print_list(num_list,mix_num_list)




