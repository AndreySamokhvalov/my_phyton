def input_string():
    list_string = input(f'Введите список ( строки без пробелов) ')
    list_string = list_stingsplit(' ')
    return list_string

def find_numbers_in_list(list_string,number):
    if number in item:
        print(f'В элементе списка {item} есть число {number} ')
    return

list_string = input_string()
print(f'Список строк {list_string}')
number = input('Введите число, которое вы хотите найти в списке')
find_numbers_in_list(list_string, number)