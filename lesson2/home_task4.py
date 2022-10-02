# . Задать список из N элементов, 
# заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions

import os
os.system("cls")
print('Добро пожаловать!')

# получение входных данных 
def input_data():
    input_num = int(input("Введите значение N: "))
    os.system("cls")
    return input_num

# заполнение списка
def creating_a_list(number):
    data_list = []
    first = abs(number)
    second = first*(-1)
    for i in range(second,first+1):
        data_list.append(i)
    return data_list

# печать результата
def print_result(input_num, out_list):
    position = []
    i = 0
    result = 1
    with open('d:/AndyData/my_phyton/lesson2/position.txt', 'r') as f:
     position = [line.strip() for line in f if line.strip()]
    print(f'Список элементов от -{input_num} до {input_num}: {out_list}')
    while i < len(position):
        if int(position[i]) > input_num*2+1:
            print (f'Индекс i={position[i]} за пределами списка')
        else:
            result = result * out_list[int(position[i])]
        i+=1
    print(f' Произведение элементов находящихся на позициях {position} равно {result}')


num = input_data()
creating_a_list(num)
print_result(num,creating_a_list(num))