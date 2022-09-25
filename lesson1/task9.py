# Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти.
import os
os.system("cls")
print('Добро пожаловать!')

def quarter_number():
    number = int(input("Введите номер четверти: "))
    if 0 < number < 5:
        if number == 1:
            print(f'Для {number}-ой четверти (X > 0) и (Y > 0)')
        elif number == 2:
            print(f'Для {number}-ой четверти (X < 0) и (Y > 0)')
        elif number == 3:
            print(f'Для {number}-ей четверти (X < 0) и (Y < 0)')
        elif number == 4:
            print(f'Для {number}-ой четверти (X > 0) и (Y < 0)')
    else:
        print('Четверти с таким номером не существует')


quarter_number()
