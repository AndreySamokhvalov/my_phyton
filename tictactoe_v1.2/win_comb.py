from tictactoe import Board
import time
import os
import emoji
import sys
board = Board(dimensions=(3,3))
lx=[1,2,3]

def aaa(lx,board):
    if ((lx.count(1)>0 and lx.count(2)>0 and lx.count(3)>0)or 
    (lx.count(4)>0 and lx.count(5)>0 and lx.count(6)>0) or
    (lx.count(7)>0 and lx.count(8)>0 and lx.count(9)>0)or
    (lx.count(1)>0 and lx.count(4)>0 and lx.count(7)>0)or
    (lx.count(2)>0 and lx.count(5)>0 and lx.count(8)>0)or
    (lx.count(3)>0 and lx.count(6)>0 and lx.count(9)>0)or
    (lx.count(1)>0 and lx.count(5)>0 and lx.count(9)>0)or
    (lx.count(3)>0 and lx.count(5)>0 and lx.count(9)>0)):
        print(board)
        print(emoji.emojize('Х - победил :partying_face:'))
        time.sleep(3)
        sys.exit()


def bbb(lo,board):
    if ((lo.count(1)>0 and lo.count(2)>0 and lo.count(3)>0)or 
    (lo.count(4)>0 and lo.count(5)>0 and lo.count(6)>0) or
    (lo.count(7)>0 and lo.count(8)>0 and lo.count(9)>0)or
    (lo.count(1)>0 and lo.count(4)>0 and lo.count(7)>0)or
    (lo.count(2)>0 and lo.count(5)>0 and lo.count(8)>0)or
    (lo.count(3)>0 and lo.count(6)>0 and lo.count(9)>0)or
    (lo.count(1)>0 and lo.count(5)>0 and lo.count(9)>0)or
    (lo.count(3)>0 and lo.count(5)>0 and lo.count(9)>0)):
        print(board)
        print(emoji.emojize('O - победил :partying_face:'))
        time.sleep(3)
        sys.exit()
