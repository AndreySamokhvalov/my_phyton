import time
from get_person import get_new_person
#from start      import person_list_menu
import os
os.system("cls")




# поиск по ключевому слову
def find_person():
    with open('directory.txt', 'r', encoding='utf-8') as a:
        spisok = [line.strip() for line in a if line.strip()]
    fnd = input('Введите ключевое слово (имя, фамилия, номер телефона, возраст, город или должность): ')
    count = 0
    print('')
    print(' №    Имя         Фамилия    тел.       Возраст    Город    Должность')
    for i in range(0, len(spisok)):
        if fnd.title() in spisok[i]:
          if i+1<10:
            print(f'{"_"* 75}')
            print(f' {i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
            count += 1
          else:
            print(f'{"_"* 75}')
            print(f'{i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
            count += 1 
    print('')
    if count == 0:
        print(f'Поиск по "{fnd.title()}" не дал результата')
        new = input('Хотите создать новый контакт?(да/нет): ')
        if new == 'да':
            os.system("cls")
            print('Создание нового контакта')
            get_new_person()
        else:
            os.system("cls")


# удаление контакта
def del_person():
    with open('directory.txt', 'r', encoding='utf-8') as a:
        spisok = [line.strip() for line in a if line.strip()]
        print(' №    Имя         Фамилия    тел.       Возраст    Город    Должность')
        for i in range(0, len(spisok)):
          if i+1<10:
            print(f'{"_"* 75}')
            print(f' {i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
          else:
            print(f'{"_"* 75}')
            print(f'{i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
    num = int(input('введите номер удаляемого контакта: '))
    os.system("cls")
    if 0 < num < len(spisok):
        tmp = input(f'Вы действительно хотите удалить контакт: "{spisok[num-1]}" ? (да/нет): ')
        if tmp == "да":
         print(f'Контакт {spisok[num-1]} удален')
         time.sleep(3)
         os.system("cls")
         spisok.pop(num-1)
         with open("directory.txt", "w", encoding='utf-8') as file:
            for line in spisok:
                file.write(line + '\n')
        elif tmp == "нет":
            os.system("cls")
        else:
            os.system("cls")
            print('неверный ввод')
            time.sleep(3)
            os.system("cls")

    else:
        os.system("cls")
        print('Такого контакта не существует!')
        time.sleep(3)
        os.system("cls")


# изменение контакта
def change_person():
    data = ['Имя', 'Фамилия', 'Номер телефона', 'Возраст', 'Город', 'Должность']
    with open('directory.txt', 'r', encoding='utf-8') as a:
        spisok = [line.strip() for line in a if line.strip()]
        print(' №    Имя      Фамилия       тел.       Возраст    Город    Должность')
        for i in range(0, len(spisok)):
          if i+1<10:
            print(f'{"_"* 75}')
            print(f' {i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
          else:
            print(f'{"_"* 75}')
            print(f'{i+1}|  {spisok[i]}')
            print(f'{"-"* 75}')
    num = int(input('Введите номер изменяемого контакта: '))
    os.system("cls")
    print(spisok[num-1]+'\n')
    change_list = list(spisok[num-1].split())
    change_person = []
    for i in range(0, len(change_list)):
        tmp = input(
            f'{data[i]}: |{change_list[i]}| введите новое значение или Enter(оставить текущее): ')
        if len(tmp) != 0:
            change_person.append(tmp.title())
        else:
            change_person.append(change_list[i].title())
    change_person[0] = str(change_person[0]).ljust(10," ")
    change_person[1] = str(change_person[1]).ljust(10," ")
    change_person[2] = str(change_person[2]).rjust(11,"8")
    change_person[3] =str(change_person[3]).rjust(6," ")
    change_person[4] =str(change_person[4]).rjust(10," ")
    change_person[5] =str(change_person[5]).rjust(10," ")
    change_str = (" ".join(change_person))
    os.system("cls")
    print(f'Контакт изменен: {change_str}')
    time.sleep(3)
    spisok[num-1] = change_str
    with open("directory.txt", "w", encoding='utf-8') as file:
        for line in spisok:
            file.write(line + '\n')



# печать всего справочника
def print_all_person():
    with open('directory.txt', 'r', encoding='utf-8') as a:
        spisok = [line.strip() for line in a if line.strip()]
    print(f'{"_"* 75}')
    print(' №    Имя      Фамилия       тел.       Возраст    Город    Должность')
    for i in range(0, len(spisok)):
        if i+1<10:
         print(f'{"_"* 75}')
         print(f' {i+1}|  {spisok[i]}')
         print(f'{"-"* 75}')
        else:
         print(f'{"_"* 75}')
         print(f'{i+1}|  {spisok[i]}')
         print(f'{"-"* 75}')
