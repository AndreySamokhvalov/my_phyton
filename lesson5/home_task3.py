import os
os.system("cls")

print('Классические крестики-нолики. Крестик ходит первым')

pole = list(range(1,10))

# рисуем поле
def make_pole(pole):
    print ("-" * 13)
    for i in range(3):
        print ("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
        print ("-" * 13)

# организум ход игрока
def take_input(player_token):
    mean = False
    while not mean:
        player_move = input("Куда ставим " + player_token+"? ")
        os.system("cls")
        try:
            player_move = int(player_move)
        except:
            print ("Вы ввели не число. Попробуйте еще раз")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(pole[player_move-1]) not in "XO"):
                pole[player_move-1] = player_token
                mean = True
            else:
                make_pole(pole)
                print ("Эта клетка уже занята")
        else:
            print ("Клетки с таким номером не существует. Введите цифру от 1 до 9.")

# выигрышные комбинаци
def win_comb(pole):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if pole[each[0]] == pole[each[1]] == pole[each[2]]:
            return pole[each[0]]
    return False

# алгоритм игры
def game(pole):
    count = 0
    win = False
    while not win:
        make_pole(pole)
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        count += 1
        if count > 4:
            tmp = win_comb(pole)
            if tmp:
                print (tmp, "победил!")
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    make_pole(pole)

game(pole)