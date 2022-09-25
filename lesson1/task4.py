# Показать первую цифру дробной части числа.
import os
os.system("cls")

print('Добро пожаловать!')
num = float(input("Введите дробное число: "))

round_num = int(num) 

result = (num - round_num)*10  

print(f'первая цифра дробной части: {int(result)}')
