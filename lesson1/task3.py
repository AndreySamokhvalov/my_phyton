# Вывести на экран числа от -N до N.
import os
os.system("cls")
print('Добро пожаловать!')
num = int(input("Введите целое число: "))


def print_num(number):
    number = abs(number)
    first = number*-1
    second = number
    while first < second:
        print(f' {first},', end='')
        first += 1
    print(f' {second}')

print_num(num)
