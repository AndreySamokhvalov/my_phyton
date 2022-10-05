import random
import os
os.system("cls")
print('Добро пожаловать!')

# получение данных
def input_data():
    input_num = int(input("Введите значение N: "))
    os.system("cls")
    return input_num
    
# фибоначи     
def fib(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    return fib(n-1) + fib(n-2) 

# негафибоначи
def nega_fib(n):
    list_nega_fib = []
    for i in range(1,n + 1):
        fibo_i = fib(i)
        list_nega_fib.append(fibo_i)
        if i != 1:
            list_nega_fib.insert(0,(-1)**(i)*fibo_i)
    print(f'Негафибоначи: {list_nega_fib}')


num = input_data()
fib(num)
nega_fib(num)
