#Реализуйте RLE алгоритм: реализуйте 
#модуль сжатия и восстановления данных.

import os
os.system("cls")    

# алгоритм сжатия данных
def text_rle(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

# алгоритм декодирования
def text_decode(text):


    result = ''
    count = ''
    for simbol in text:
        if simbol.isdigit():
            count += simbol
        else:
            result += simbol * int(count)
            count = ''
    return result


with open('origin.txt', 'r') as file:
    origin = file.readline()

result_rle = text_rle(origin)

with open('result_rle.txt', 'w') as file:
    file.write(f'{result_rle}')


with open('origin_rle.txt', 'r') as file:

    origin_rle = file.readline()

res_decode = text_decode(origin_rle)

with open('res_decode.txt', 'w') as file:
    file.write(f'{res_decode}')




