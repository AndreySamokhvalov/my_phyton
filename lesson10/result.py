import os
os.system("cls")


def save_result(out_list):
    with open("result.txt", "w", encoding='utf-8') as file:
        lines = " ".join(map(str, out_list))
        for line in lines:
            file.write(line)
            os.system("cls")
    print('Результат сохранен в "result.txt"')
