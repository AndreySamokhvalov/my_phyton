import sqlite3

data_base = sqlite3.connect('Data_base.db')

cursor = data_base.cursor()

cursor.execute('''Create table if not exists personal(
    id INTEGER,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
)''')


base = [(1,"Иван","Байда","Главный по тарелочкам",50000,10000),
(2,"Петр","Брунька","Повар",50500,10200),
(3,"Олег","Лысый-Цой","Администратор",70000,15000)]
#name = input('Введите имя: ')

try:
    cursor.executemany('INSERT INTO personal values(?,?,?,?,?,?)',base)
    data_base.commit()
except:
    print("данные уже есть")

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)

#cursor.execute('DELETE from personal WHERE id = 1')

# cursor.execute('select * from personal WHERE name LIKE "Олег";')
# one = cursor.fetchmany()
# print(*one)

cursor.execute('SELECT * from personal WHERE name LIKE "Олег";')
one = cursor.fetchone()
print(one)

cursor.execute('DELETE from personal WHERE id = 1')
data_base.commit()

def previev_base():
    pass

def add_record():
    pass

def delete_record():
    pass

def find_record():
    pass

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)

def input_choice():
    while True:
        user_choise = input('1 - посмотреть базу\n'
        '2 - добавить запись\n' 
        '3- удалить запись\n'
        ' 4 - найти по ФИО\n'
        '5 - редактировать запись\n' 
        '* - выход\n')
        if user_choise == "1":
            previev_base()
        elif user_choise == "2":
            add_record()
        elif user_choise == "3":
            delete_record()
        elif user_choise == "4":
            find_record()
        elif user_choise == "5":
            find_record()
        elif user_choise == "q":
            print('Выход')
            break
        else:
            print('Ошибка ввода')
        

cursor.execute('UPDATE personal SET salary = 55000 WHERE id=2')
data_base.commit()

for i in cursor.execute('SELECT * FROM personal'):
    print(*i)





