# Найти максимальное из пяти чисел.
import os
os.system("cls")


def input_data():
 print('Добро пожаловать!')
 numbers = []
 numbers.append(int(input("Введите первое число: ")))
 numbers.append(int(input("Введите второе число: ")))
 numbers.append(int(input("Введите третье число: ")))
 numbers.append(int(input("Введите четвертое число: ")))
 numbers.append(int(input("Введите пятое число: ")))
 os.system("cls")
 print(numbers)
 return numbers

def find_max_index(list):
    i = 0 
    max=list[0]
    while i < len(list):
        if list[i]>max:
            max=list[i]
        i+=1
    return max

num = input_data()
print('Максимальное из введенных чисел: ',find_max_index(num))
