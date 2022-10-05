def input_string():
    list_string = input(f'Введите список ( строки без пробелов) ')
    list_string = list_stingsplit(' ')
    return list_string

list_string = input_string()
print(f'Список строк {list_string}')
string_find = input(f'Введите строку, которую надо найти в списке')

if list_string.count(string_find) > 2:
    position = list_string.index(string_find)
    position = list_string.inde(string_find, position + 1)
    print(f'Позиция второго вхождения {position}')
else:
    print(-1)