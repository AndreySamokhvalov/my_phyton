import sys
import os
from pic         import logo
from command     import print_all_person
from command     import find_person
from command     import change_person
from command     import del_person
from get_person  import get_new_person
from export_file import format_save
#from command    import format_save
os.system("cls")
print('Добро пожаловать!')

def person_list_menu():
    logo()
    while True:
        
        print('1 - посмотреть весь справочник \n'
              '2 - добавить новый контакт \n'
              '3 - поиск по ключевому слову\n'
              '4 - редактировать контакт \n'
              '5 - удалить контакт \n'
              '6 - экспорт справочника \n'
              '* - выход ')

        enter = input(': ')
            
        if enter == '1':
            os.system("cls")
            print_all_person()
        elif enter == '2':
            os.system("cls")
            get_new_person()
        elif enter == '3':
            os.system("cls")
            find_person()
        elif enter == '4':
            os.system("cls")
            change_person()
        elif enter == '5':
            os.system("cls")
            del_person()
        elif enter == '6':
            os.system("cls")
            format_save()
            
        elif enter == '*':
            os.system("cls")
            print ('До свидания!')
            print('')
            break
        else:
           print ('Команда указана неверно!')

person_list_menu()