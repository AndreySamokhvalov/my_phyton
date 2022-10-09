# Вычислить число c заданной точностью d
import math
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_str = input("Введите значение точностии: ")
    os.system("cls")
    return input_str

# обработка данных
def calk_accuracy(input_string):
    accuracy = input_string.split('.')
    accuracy = len(accuracy[1])
    return accuracy

# печать результата
def print_accuracy(v,out_str):
    print(f'Число Pi с точностью {out_str} = {round(math.pi,v)}')


data_str = input_data()
calk_accuracy(data_str)
print_accuracy(calk_accuracy(data_str),data_str)
