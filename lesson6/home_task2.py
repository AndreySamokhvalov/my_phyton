#Для натурального n создать список,
#состоящий из элементов последовательности 3n + 1
import os
os.system("cls")

# ввод данных
def input_data():
    imput_num = int(input("Введите значение N: "))
    return imput_num

# создание листа 
def creating_a_list(num):
    # использую:
    result_list = map(lambda x: 3*x+1, range (1, num+1))

    #вместо:
    # result_list = []
    # for i in range(1,num+1):
    #  result_list.append(3*i+1)
    print(list(result_list))

number = input_data()
creating_a_list(number)