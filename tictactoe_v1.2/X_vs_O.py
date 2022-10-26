# Крестики - нолики на базе сторонней библиотеки python-tictactoe v0.0.7

from tictactoe import Board
from win_comb import aaa
from win_comb import bbb
import os
import emoji
import time
os.system("cls")



print('Классические крестики-нолики.\n'
      'Крестик ходит первым')
time.sleep(2)
os.system("cls")

board = Board(dimensions=(3,3))

# определение хода
count = 0

# списки ходов
lx = []
lo = []


while count < 9:
    print(board)
    if count%2 == 0:
        
        token = int(input('Ходит крестик: '))
        if (token in lx) or (token in lo):
            print (f'Клетка {token} уже занята! Попробуйте еще раз')
            time.sleep(2)
            os.system("cls")
        else:
            if token == 1:
                board.push((0, 0))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 2:
                board.push((1, 0))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
                
            elif token == 3:
                board.push((2, 0))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 4:
                board.push((0, 1))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 5:
                board.push((1, 1))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 6:
                board.push((2, 1))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 7:
                board.push((0, 2))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 8:
                board.push((1, 2))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            elif token == 9:
                board.push((2, 2))
                os.system("cls")
                lx.append(token)
                aaa(lx,board)
                count+=1
            else:
                print('Ничья!')
    else:
        token = int(input('Ходит нолик: '))
        if (token in lx) or (token in lo):
            print (f'Клетка {token} уже занята! Попробуйте еще раз')
            time.sleep(2)
            os.system("cls")
        else:
            if token == 1:
                board.push((0, 0))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            elif token == 2:
                board.push((1, 0))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
                
            elif token == 3:
                board.push((2, 0))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            elif token == 4:
                board.push((0, 1))
                os.system("cls")
                lo.append(token)
                count+=1
            elif token == 5:
                board.push((1, 1))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            elif token == 6:
                board.push((2, 1))
                lo.append(token)
                bbb(lo,board)
                os.system("cls")
                count+=1
            elif token == 7:
                board.push((0, 2))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            elif token == 8:
                board.push((1, 2))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            elif token == 9:
                board.push((2, 2))
                os.system("cls")
                lo.append(token)
                bbb(lo,board)
                count+=1
            else:
                print('Ничья!')



