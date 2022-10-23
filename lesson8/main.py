import sys
import os
import sqlite3
os.system("cls")
# from create_base import new_data_base
from model import previev_base
from model import add_record
from model import find_record
from model import delete_record
from model import update_base

print('Добро пожаловать!')

def input_choice():
    while True:
        user_choise = input(
            '1 - посмотреть базу\n'
            '2 - добавить запись\n' 
            '3 - поиск записи\n'
            '4 - редактирование записи\n'
            '5 - удаление записи\n' 
            '* - выход\n')
        if user_choise == "1":
            previev_base()
        elif user_choise == "2":
            add_record()
        elif user_choise == "3":
            find_record()
        elif user_choise == "4":
            update_base()
        elif user_choise == "5":
            delete_record()
        elif user_choise == "*":
            os.system("cls")
            print('Выход')
            break
        else:
            print('Ошибка ввода')

input_choice()
