#Подсчитать сумму цифр в вещественном числе

import os
os.system("cls")
print('Добро пожаловать!')

# ввод данных
def input_data():
    imput_str = input("Введите вещественное число: ")
    os.system("cls")
    if (imput_str.count('.')== False):
        print(f'Число {imput_str} - не вещественное, будет использовано число {str(float(imput_str)+.0)}')
        return str(float(imput_str)+.0)
    else:
     return imput_str

# преобразование строки
def string_conversion(string):
    new_string = string.replace('.', '')
    return(new_string)

# сложение цифр в вещественном числе
def calculete(final_string):
    result = 0
    for i in range (len(final_string)):
        result = result + int(final_string[i])
    return result

# печать результата
def print_result(out_string,out_number):
    print(f'Сумма цифр в вещественном числе {out_string} равна {out_number}')


num = input_data()
string_conversion(num)
calculete(string_conversion(num))
print_result(num,calculete(string_conversion(num)))


