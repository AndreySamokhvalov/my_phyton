import os
import time
os.system("cls")


def format_save():
    print('По умолчанию файл сохранен в формате ".txt"\n'
          'Если вы хотите экспортировать справочник в формат ".csv" - нажмите 1\n'
          'Если вы хотите экспортировать справочник в формат ".md" - нажмите 2\n'
          'Для выхода - нажмите *')
    form = input(': ')
    if form == '1':
        with open('directory.txt', 'r', encoding='utf-8') as a:
         spisok = [line.strip() for line in a if line.strip()]

        with open("directory.csv", "w", encoding='utf-8') as file:
         for line in spisok:
            file.write(line + '\n')
        os.system("cls")
        print('Файл экспортирован в формат ".cvs"')
        time.sleep(3)
        os.system("cls")
    elif form == '2':
        with open('directory.txt', 'r', encoding='utf-8') as a:
         spisok = [line.strip() for line in a if line.strip()]

        with open("directory.md", "w", encoding='utf-8') as file:
         for line in spisok:
            file.write(line + '\n')
        os.system("cls")
        print('Файл экспортирован в формат ".md"')
        time.sleep(3)
        os.system("cls")
    elif form == '*':
        os.system("cls")
        print('Файл сохранен только в формате ".txt"')
        time.sleep(3)
        os.system("cls")
    else:
        print('неверный ввод')
        time.sleep(3)
        os.system("cls")
