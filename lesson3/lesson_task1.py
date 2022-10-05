import time
import random
import os
os.system("cls")
print('Добро пожаловать!')
print(' Программа выдает псевдослучайное число в интервале от 0 до В')
# a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

y = time.time_ns()

line = str(y)
new_line = line[-7:-4]

if b > 0:
    if b < 10:
     result = int(new_line)%10
     if result > b:
      while result > b :
                result = round(result/2)
    elif b < 100:
     result = int(new_line)%100
     if result > b and b%2==0  :
      while result > b :
                result = round(result/2)%100
     elif result > b and b%3==0  :
        while result > b :
                result = round(result/2)%10
     elif result > b  :
        while result > b  :
                result = round(result/2)
    elif b < 1000:
     result = int(new_line)
     if result > b and b%2==0  :
      while result > b :
                result = round(result/2)%100
     elif result > b and b%3==0  :
        while result > b :
                result = round(result/2)%10
     elif result > b   :
        while result > b :
                result = round(result/2)

print(f'результат- {result}')

rand_x = int((int(new_line[0])+int(new_line[1]))/2)
print(new_line)

print(rand_x)
