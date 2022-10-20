import time
import os
os.system("cls")


def get_new_person():
    namex = input('Введите имя контакта: ')
    name = namex.ljust(10," ")
    familyx = input('Введите фамилию контакта: ')
    family = familyx.ljust(10," ")
    numberx = input('Введите номер контакта в десятизначном формате: ')
    number = numberx.rjust(11,"8")
    agex = input('Введите возраст контакта: ')
    age = agex.rjust(6," ")
    geox = input('Город проживания: ')
    geo = geox.rjust(10," ")
    jobx = input('Должность: ')
    job = jobx.rjust(10," ")
    info = [name.title(),family.title(),number.title(),age,geo.title(),job.title()]
    info_str = (" ".join(info))
    print(info_str)
    with open('directory.txt', 'a', encoding='utf-8') as data:
     data.write('\n' + info_str)
    os.system("cls")
    print(f'Контакт записан: {info_str}')
    time.sleep(3)
    os.system("cls")
