# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
import os
import os
os.system("cls")

with open('message.txt', 'r', encoding='utf-8') as a:
     message = [line.strip() for line in a if line.strip()]

with open('massage_candies_total.txt', 'r', encoding='utf-8') as b:
     massage_candies_total = [line.strip() for line in b if line.strip()]

with open('massage_game_over.txt', 'r', encoding='utf-8') as c:
     massage_game_over = [line.strip() for line in c if line.strip()]

with open('message_candymen.txt', 'r', encoding='utf-8') as d:
     message_candymen = [line.strip() for line in d if line.strip()]


print('Приветствую тебя, любитель конфет!\n'
      'Меня зовут Кэндимен, и я хочу сыграть с тобой в игру!\n'
      'Суть в такова: на столе лежат конфеты, два игрока по очереди\n'
      'берут от 1 до 28 конфет. Выигрывает тот, кто заберет последние конфеты со стола.\n'
      'Есть два режима на выбор: "игра со мной" и "игра с другом"\n'
      'Чтобы сыграть со мной - введи "pve"\n'
      'Чтобы сыграть с другом - введи "pvp"\n')



game_mode=(input('Какой режим игры ты выберешь?: '))

# режим человек против человека
def p_v_p():
    os.system("cls")
    print('Два друга сошлись в конфетной битве!!!')
    player_1 = input('Как мне обращаться к первому игроку? ')
    player_2 = input('Второй игрок, как зовут тебя? ')
    os.system("cls")
    print('Отлично, с именами разобрались!')
    candies_total = int(input('Давайте решим, сколько конфет на кону?: '))
    os.system("cls")
    print('Чтож, пусть будет так))')
    max_take = 28
    min_take = 1
    count = 0
    print('Теперь определим, кто делает первый ход!')
    print('Я загадаю число от 1 до 10. Вы по очереди назовете свое число')
    print('Чье число будет ближе к загаданному мной, тот и начинает!)')
    attempt_1 = int(input(f'{player_1}, предлагай свой вариант: '))
    attempt_2 = int(input(f'{player_2}, теперь твоя очередь: '))
    os.system("cls")

    x = random.randint(1, 10)

    if abs(x-attempt_1) == abs(x-attempt_2):
        lucky = player_1
        loser = player_2
        print(f'Я загадал число {x}. Похоже ничья. В этом случае первый ход делает {lucky} )')
        print(f'Ну чтож {player_1} и  {player_2}, на кону {candies_total} конфет!')
        print('Игра началась!')
    else:
     if abs(x-attempt_1) < abs(x-attempt_2):
        lucky = player_1
        loser = player_2
     else:
        lucky = player_2
        loser = player_1
     print(f'Я загадал число {x}. Похоже {lucky} оказался ближе)')
     print(f'Значит {lucky} ходит первым!')
     print(f'Ну чтож {player_1} и  {player_2}, на кону {candies_total} конфет!')
     print('Игра началась!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{random.choice(message)}, {lucky}: '))
            if step > candies_total or step > max_take or step < min_take:
                step = int(input(f'\nТы можешь взять от {min_take} до {max_take} конфет, но не больше, чем {candies_total}, {lucky}. Подумай и попробуй еще разок: '))
            candies_total = candies_total - step
        if candies_total > 0:
            os.system("cls")
            print(f'\n{random.choice(massage_candies_total)} {candies_total} конфет')
            count = 1
        else:
            os.system("cls")
            print(F'{random.choice(massage_game_over)}')

        if count == 1:
            step = int(input(f'\n{random.choice(message)}, {loser}: '))
            if step > candies_total or step > max_take or step < min_take:
                step = int(input(f'\nТы можешь взять от {min_take} до {max_take} конфет, но не больше, чем {candies_total}, {loser}. Подумай и попробуй еще разок: '))
            candies_total = candies_total - step
        if candies_total > 0:
            os.system("cls")
            print(f'\n{random.choice(massage_candies_total)} {candies_total} конфет')
            count = 0
        else:
            os.system("cls")
            print(F'{random.choice(massage_game_over)}')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ(А)')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ(А)')

# режим человек против компьютера
def p_v_e():

    max_take = 28
    min_take = 1
    os.system("cls")
    print('Я и ты! Один на один!')
    print('Кто ты, воин?')
    player_1 = input(':')
    player_2 = 'Кэндимен'
    x = random.randint(1, 10)
    rand = random.randint(1, 10)
    print(f'Ну чтож {player_1}, давай сыграем)!')
    candies_total = int(input('Сперва решим, сколько конфет на кону?: '))
    os.system("cls")
    print('Теперь опеределим кто первый начнет игру.')
    print('Мы по очереди назовем число от 0 до 10')
    print('Генератор псевдослучайных чисел выдаст свое число')
    print('Чье число будет ближе к сгенерированному, тот и начинает!)')
    print(f'Мое число : {x}')
    attempt_1 = int(input(f'{player_1}, предлагай свой вариант: '))
    print(f'Псевдослучайное число - {rand}')
    if abs(rand-attempt_1) == abs(rand-x):
        lucky = player_1
        count = 1
        print(f'Псевдослучайное число - {rand}. Ого, ничья! Раз уж ты мой гость, начинай первым))')
        # print(f'Чтож {player_1}, на кону {candies_total} конфет!')
        # print('Игра началась!')
    else:
     if abs(rand-attempt_1) < abs(rand - x):
        lucky = player_1
        count = 1
     else:
        lucky = player_2
        count = 0

    print(f'Похоже {lucky} ходит первым!')
    print('Поехали!')

    while candies_total > 0:

        if  count == 0:
            print(' ')
            #print(f'На кону {candies_total}. Мой ход!')
            print('Кэндимен:')

            if candies_total < 29:
                step = candies_total
            elif 87<candies_total<115:
                step = candies_total - 87
            elif 58<candies_total<87:
                step = candies_total - 58
            elif 29<candies_total<58:
                step = candies_total - 29
            elif candies_total==30:
                step = 1
            else:
                 step = random.randint(1,28)

            print(f'На кону {candies_total}. {random.choice(message_candymen)} Я возьму {step}')   
            count = 1
        else:
            print(' ')
            step = int(input(f'На кону {candies_total}. {random.choice(message)}:  '))
            os.system("cls")
            while step > max_take or step > candies_total or step < min_take:
                step = int(input(f'\nТы можешь взять от {min_take} до {max_take} конфет, но не больше, чем осталось на столе, {player_1}. Подумай и попробуй еще разок: '))
            count = 0
        candies_total = candies_total - step
        
        

    print(F'{random.choice(massage_game_over)}')

    if count == 1:
        print('')
        print(f'{player_2}: Я СНОВА ПОБЕДИЛ!')
        print('')
    if count == 0:
        print('')
        print(f'ТЫ ПОБЕДИЛ(А) {player_1}, МОИ ПОЗДРАВЛЕНИЯ!')
        print('')



if game_mode == 'pve':
    p_v_e()
elif game_mode == 'pvp':
    p_v_p()
else:
    os.system("cls")
    print('Не хочешь - не играй!')
    print('Если передумаешь, ты знаешь, где меня найти)')
