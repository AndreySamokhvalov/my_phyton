# Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.
import os
os.system("cls")

# ввод данных
def input_data():
    imput_num = int(input("Введите значение N: "))
    return imput_num

# создание последовательности
def sequence(number):
    result_list = []
    i = 0  
    while i < number:
        result_list.append(int(3**i))
        if i % 2 != 0:
            result_list[i] = result_list[i] * (-1)
        i += 1
    print(*result_list, sep=", ")


num = input_data()
sequence(num)
