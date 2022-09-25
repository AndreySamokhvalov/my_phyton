# 5 Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30
import os
os.system("cls")
print('Добро пожаловать!')

num = int(input("Введите целое число: "))


def find(number):
    if number%30 !=0:
        if number%5==0 and number%10==0 or number%15==0:
            return "число кратно"
    return "число  не кратно"     

print(find(num))
