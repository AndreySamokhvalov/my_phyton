# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв"".
import os
os.system("cls")
print('Добро пожаловать!')

# получение текста из файла
def read_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        line = data.read()
        print(f'Исходный текст: {line}')
    return line

# удаляем слова включающее в себя указанное сочитание букв
def delit_simbol(input_str):
    words = input_str.split(' ')
    simbol = 'абв' # 'абв' - не разобрался с кодировками
    new_words = []
    for word in words:
        if simbol not in word:
            new_words.append(word)
    line_out = ' '.join(new_words)
    print(f"Модифицированный текст: {line_out} ")
    new_line = ' '.join(new_words)
    # запись в файл
    with open(out_file, 'w', encoding='utf-8') as data:
     data.write(new_line)
    print(f'Измененнный текст записан в файл {out_file}')

file_name ='origin_file.txt'
out_file = 'out_file.txt'
in_str = read_data(file_name)
delit_simbol(in_str)
