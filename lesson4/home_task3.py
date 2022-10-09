#Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.
import random
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_str = input("Введите элементы через пробел: ")
    os.system("cls")
    return input_str

# формируем список
def list_creating(input_str):
    input_list = []
    input_list = input_str.split(sep=' ')
    return input_list

# удаляем повторяющиеся элементы
def list_conversion(original_list):
    set_number = set(original_list)
    original_list = list(set_number)
    return original_list

# список уникальных элементов
def non_repeat(number_lst):
    non_repeat_list = []
    for elem in number_lst:
        if number_lst.count(elem) == 1:
            non_repeat_list.append(elem)
    return non_repeat_list

# список повторяющихся элементов
def repeat_elements(number_lst):
    repeat_list = []
    for elem in number_lst:
        if number_lst.count(elem) > 1:
            repeat_list.append(elem)
    return list(set(repeat_list))



# печать результата
def print_result(first_list,second_list,third_list,fourth_list):
    print(f'Введеный список элементов: {first_list}')
    print(f'Список без повторяющихся элементов: {second_list}')
    print(f'Список уникальных элементов: {third_list}')
    print(f'Список повторяющихся элементов: {fourth_list}')
    

str = input_data()
list_creating(str)
list_conversion(list_creating(str))
non_repeat(list_creating(str))
repeat_elements(list_creating(str))
print_result(list_creating(str),list_conversion(list_creating(str)),non_repeat(list_creating(str)),repeat_elements(list_creating(str)))
