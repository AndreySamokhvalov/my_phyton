# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
import random
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_num = int(input("Задайте число N: "))
    return input_num

# создание списка простых множителей
def prime_factors(number):
    if number <= 2:
        print('Введено некорректное чило')
    else:
        simple_lst = []
        while number > 1:
            for i in range(2, number+1):
                if number%i == 0:
                 if check_simple(i):
                    simple_lst.append(i)
                    number //=i
                    break
        return simple_lst

# проверка на натуральность
def check_simple(simple_num):
    for i in range(2,(simple_num//2+1)):
        if (simple_num%i==0):
            return False
    return True

# печать результата
def print_result(out_num, out_lst):
    print(f'Cписок простых множителей числа {out_num}: {out_lst}')

num = input_data()
prime_factors(num)
print_result(num,prime_factors(num))

