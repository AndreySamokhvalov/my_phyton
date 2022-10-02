# Задать список из n чисел последовательности 
#  (1 + 1/n)^n и вывести на экран их сумму

import os
os.system("cls")
print('Добро пожаловать!')

# получение входных данных
def input_data():
    input_num = int(input("Введите значение n: "))
    #os.system("cls")
    return input_num

# создание списка
def creating_a_list(number):
    data_list = []
    for i in range (1,number+1):
        data_list.append((1+1/i)**i)
    return data_list

# нахождение суммы элементов списка
def calculete(input_list):
    result = 0
    i = 0
    while i < len(input_list):
        result = result + input_list[i]
        i+=1
    return result

# печать результата
def print_result(input_num):
    print(f'Cумма чисел последовательности равна {input_num}')

num = input_data()
creating_a_list(num)
calculete(creating_a_list(num))
print_result(calculete(creating_a_list(num)))