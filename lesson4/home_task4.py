#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
import random
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_num = abs(int(input("Введите степень многочлена: ")))
    return input_num

# создание словаря 
def degree_of_the_polynomial(number):
    degree = {}
    while number != -1:
        cof = random.randint(0,101)
        degree[number] = cof
        number -= 1
    return degree

# формирование многочлена и запись в файл
def creating_polynomial(degree_dict, file_name):
    text_string = ''
    max_degree = max(degree_dict.keys())
    for degree in range(max_degree,-1,-1):
        if degree_dict[degree] !=0:
            if degree_dict[degree] > 0:
                sign = '+'
            else:
                sign = '-'
            if abs(degree_dict[degree]) == 1 and degree !=0:
                temp = ''
            else:
                temp = str(abs(degree_dict[degree]))
            if degree == 0:
                text_string += sign + ' ' + temp
            elif degree ==1:
                text_string += sign + ' ' + temp + 'x '
            else:
                text_string += sign + ' ' + temp + f'x^{degree} '
    if text_string[-1] == ' ':
        text_string += '= 0'
    else:
        text_string += '= 0'
    if text_string[0] == '+':
        text_string = text_string[2:]
    # запись многочлена в файл
    with open(file_name, 'w') as data:
        data.write(text_string)
    print(f'Многочлен {text_string} записан в файл {file_name}')


num = input_data()
p_dict = degree_of_the_polynomial(num)
file_name = 'polynomial.txt'
creating_polynomial(p_dict, file_name)