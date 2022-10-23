import time
import sys
import os
import sqlite3
#from create_base import new_data_base
os.system("cls")

# data_base = sqlite3.connect('Data_base.db')

# cursor = data_base.cursor()

# cursor.execute('''Create table if not exists personal(
#     id INTEGER,
#     name TEXT,
#     last_name TEXT,
#     position TEXT,
#     salary INT,
#     bonus INT
# )''')


# base = [(1,"Иван","Байда","Главный по тарелочкам",50000,10000),
# (2,"Петр","Брунька","Повар",50500,10200),
# (3,"Олег","Лысый-Цой","Администратор",70000,15000)]

# try:
#     cursor.executemany('INSERT INTO personal values(?,?,?,?,?,?)',base)
#     data_base.commit()
# except:
#     print("данные уже есть")


# просмотр базы
def previev_base():
    data_base = sqlite3.connect('Data_base.db')
    cursor = data_base.cursor()
    os.system("cls")
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='personal' ''')
    if cursor.fetchone()[0]==0 :
        print('База данных не найдена\n')
        num = input('Хотите создать новую запись? (да/нет): ')
        if num == 'да':
            os.system("cls")
            add_record()
        elif num == 'нет':
            os.system("cls")
            print('В базе данных 0 записей, попробуйте создать новую запись\n'
            'и повторить попытку')
            time.sleep(3)
            os.system("cls")
        else:
            os.system("cls")
            print('неверный ввод')
            time.sleep(3)
            os.system("cls")
            data_base.close()
    else :
        for i in cursor.execute('SELECT * FROM personal'):
            print(*i)
    data_base.close()


# добавления новой записи
def add_record():
    #os.system("cls")
    data_base = sqlite3.connect('Data_base.db')
    cursor = data_base.cursor()

    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='personal' ''')

    if cursor.fetchone()[0]==0 :
        cursor.execute('''Create table if not exists personal(
            name_id INTEGER PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            position TEXT,
            salary INT,
            bonus INT
            )''')

        n = input('Введите имя: ').title()
        l_n = input('Введите фамилию: ').title()
        pos = input('Введите должность: ')
        sal = int(input('Введите зарплату: '))
        bon = sal/100*25
        cursor.execute(f'''INSERT INTO personal(name,last_name,position,salary,bonus) 
                values("{n}","{l_n}","{pos}","{sal}","{bon}")''')
        os.system("cls")
        print('Запись добвалена')
        time.sleep(3)
        os.system("cls")

    else :
        n = input('Введите имя: ').title() 
        l_n = input('Введите фамилию: ').title()
        pos = input('Введите должность: ')
        sal = int(input('Введите зарплату: '))
        bon = sal/100*25
        cursor.execute(f'''INSERT INTO personal (name,last_name,position,salary,bonus)
                values("{n}","{l_n}","{pos}","{sal}","{bon}")''')
        os.system("cls")
        print('Запись добвалена')
        time.sleep(3)
        os.system("cls")
    
    data_base.commit()
    data_base.close()
    


# поиск по базе
def find_record():
    data_base = sqlite3.connect('Data_base.db')
    cursor = data_base.cursor()
    os.system("cls")
    print('Для поиска по имени - введите 1\n'
          'Для поиска по фамилии - введите 2\n'
          'Для поиска по должности - введите 3\n'
          'Для поиска по зарплате - введите 4\n')
    num = input(': ')
    if num == '1':
        rer = input('Введите имя: ')
        rer = rer.title()
        cursor.execute(f"SELECT * FROM personal WHERE name = '{rer}' ")
        one = cursor.fetchone()
        os.system("cls")
        print(f'{rer}:')
        if one is None:
            print('Запись не найдена')
            time.sleep(3)
            os.system("cls")
            
        else:
            print(*one)
            time.sleep(3)
            os.system("cls")
            
    elif num == '2':
        a = input('Введите фамилию: ')
        a = a.title()
        cursor.execute(f'SELECT * from personal WHERE last_name LIKE "{a}";')
        one = cursor.fetchone()
        os.system("cls")
        print(f'{a}:')
        if one is None:
            print('Запись не найдена')
            time.sleep(3)
            os.system("cls")
        else:
            print(*one)
            time.sleep(3)
            os.system("cls")
    elif num == '3':
        a = input('Введите должность: ')
        a = a.title()
        cursor.execute(f'SELECT * from personal WHERE position LIKE "{a}";')
        one = cursor.fetchone()
        os.system("cls")
        print(f'{a}:')
        if one is None:
            print('Запись не найдена')
            time.sleep(3)
            os.system("cls")
        else:
            print(*one)
            time.sleep(3)
            os.system("cls")
    elif num == '4':
        a = int(input('Введите зарплату: '))
        a = a.title()
        cursor.execute(f'SELECT * from personal WHERE salary LIKE "{a}";')
        one = cursor.fetchone()
        print(f'{a}:')
        if one is None:
            print('Запись не найдена')
            time.sleep(3)
            os.system("cls")
        else:
            print(*one)
            time.sleep(3)
            os.system("cls")
    else:
        os.system("cls")
        print('неверный ввод')
        time.sleep(3)
        os.system("cls")
    data_base.close()




# удаление записи
def delete_record():
    data_base = sqlite3.connect('Data_base.db')
    cursor = data_base.cursor()
    previev_base()
    del_id = input('\n Введите id удаляемой позиции: ')
    cursor.execute(f'DELETE from personal WHERE name_id = "{del_id}"')
    data_base.commit()
    os.system("cls")
    print('Контакт удален!')
    time.sleep(3)
    os.system("cls")
    data_base.close()


# изменение записи
def update_base():
    previev_base()
    data_base = sqlite3.connect('Data_base.db')
    cursor = data_base.cursor()
    upd_id = input('\n Введите id изменяемой позиции: ')
    os.system("cls")
    print('Для изменения имени - введите 1\n'
          'Для изменения фамилии - введите 2\n'
          'Для изменения должности - введите 3\n'
          'Для изменения зарплаты - введите 4\n')
    num = input(': ')
    if num == '1':
        a = input('Введите новое имя: ')
        a = a.title()
        cursor.execute(f'UPDATE personal SET name = "{a}" WHERE name_id= "{upd_id}";')
        data_base.commit()
       #cursor.execute(f'SELECT * from personal WHERE id= "{upd_id}";')
        one = cursor.fetchone()
        os.system("cls")
        print('Значение изменено:')
        time.sleep(3)
        os.system("cls")
    elif num == '2':
        a = input('Введите новую  фамилию: ')
        a = a.title()
        cursor.execute(f'UPDATE personal SET last_name = "{a}" WHERE name_id="{upd_id}";')
        data_base.commit()
        #cursor.execute(f'SELECT * from personal WHERE id= "{upd_id}";')
        one = cursor.fetchone()
        os.system("cls")
        print('Значение изменено:')
        time.sleep(3)
        os.system("cls")
    elif num == '3':
        a = input('Введите новую должность: ')
        cursor.execute(f'UPDATE personal SET position = "{a}" WHERE name_id="{upd_id}";')
        data_base.commit()
        #cursor.execute(f'SELECT * from personal WHERE id= "{upd_id}";')
        one = cursor.fetchone()
        os.system("cls")
        print('Значение изменено:')
        time.sleep(3)
        os.system("cls")
    elif num == '4':
        a = int(input('Введите новую зарплату: '))
        cursor.execute(f'UPDATE personal SET salary = "{a}" WHERE name_id="{upd_id}";')
        cursor.execute(f'UPDATE personal SET bonus = "{a/100*25}" WHERE id="{upd_id}";')
        data_base.commit()
        #cursor.execute(f'SELECT * from personal WHERE id= "{upd_id}";')
        one = cursor.fetchone()
        os.system("cls")
        print('Значение изменено:')
        time.sleep(3)
        os.system("cls")
    else:
        os.system("cls")
        print('неверный ввод')
        time.sleep(3)
        os.system("cls")
    data_base.close()
    # cursor.execute('UPDATE personal SET salary = 55000 WHERE id=2')
    # data_base.commit()

