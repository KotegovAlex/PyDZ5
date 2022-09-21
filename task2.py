# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. 

    # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
        # a) Добавьте игру против бота
        # b) Подумайте как наделить бота ""интеллектом""
import random as r
from types import NoneType

candy_number = 2021

def game_2021_candy_pvp(candys: int):
    print('''
            Игра началась! Первый ход определяется жеребьёвкой.
            За один ход можно забрать не более чем 28 конфет.
            Все конфеты оппонента достаются сделавшему последний ход.
            ''') 
    print('Рандом решит, кто будет ходить первым!!!')
    print()
    turn = r.choice([1, 2])

    # Жеребьевка
    print('Бог рандома решил, что первым будет ходить: ')
    match turn:
        case 1: 
            print('Игрок 1')
        case 2: 
            print('Игрок 2')
    
    while candys != 0:
        print()
        print(f'Количество конфет на столе: {candys}')
        if turn % 2 != 0:
            drag = int(input('Ход Игрока 1, берите конфеты => '))
        else:
            drag = int(input('Ход Игрока 2, берите конфеты => '))
        if drag > 28: 
            print('Нельзя брать больше 28 конфет за раз!!!')
            continue
        if drag < 1:
            print('Необходимо брать минимум одну конфету!!!')
            continue
        candys -= drag
        turn +=1
    else:
        if turn % 2 == 0:
            print('Игра окончена. Все конфеты получает Игрок 1')
        else:
            print('Игра окончена. Все конфеты получает Игрок 2')


def game_2021_candy_pve(candys: int):
    print('''
            Игра против бота началась! Первый ход определяется жеребьёвкой.
            За один ход можно забрать не более чем 28 конфет.
            Все конфеты оппонента достаются сделавшему последний ход.
            ''') 
    print('Чтобы определить, кто ходит первым, необходимо угадать число от 1 до 5')
    number = r.randint(1, 5)

    print('Рандом решит, кто будет ходить первым!!!')
    print()
    turn = r.choice([1, 2])

    # Жеребьевка
    print('Бог рандома решил, что первым будет ходить: ')
    match turn:
        case 1: 
            print('Игрок')
        case 2: 
            print('Бот')

    while candys != 0:
        print()
        print(f'Количество конфет на столе: {candys}')
        if turn % 2 != 0: drag = int(input('Ход Игрока, берите конфеты => '))
        else:
            if candys >= 28: drag = r.randint(1, 28)
            else: drag = r.randint(1, candys)
            print(f'Ход Бота, конфет взято => {drag}')
        if drag > 28: 
            print('Нельзя брать больше 28 конфет за раз!!!')
            continue
        if drag < 1:
            print('Необходимо брать минимум одну конфету!!!')
            continue
        if (drag > candys) and (candys < 28):
            print('На столе нет столько конфет!!!')
            continue
        candys -= drag
        turn += 1
    else:
        if turn % 2 == 0: print('Игра окончена. Все конфеты получает Игрок')
        else: print('Игра окончена. Все конфеты получает Бот')


def game_2021_candy_pve_smart(candys: int):
    print('''
            Игра против "умного" бота началась! Первый ход определяется жеребьёвкой.
            За один ход можно забрать не более чем 28 конфет.
            Все конфеты оппонента достаются сделавшему последний ход.
            ''') 
    print('Рандом решит, кто будет ходить первым!!!')
    print()
    turn = r.choice([1, 2])
    status = NoneType

    # Жеребьевка
    print('Бог рандома решил, что первым будет ходить: ')
    match turn:
        case 1: 
            print('Игрок')
        case 2: 
            print('Бот')
            status = 1
    print()
    
    # Определение действий для "умного" бота
    print(f'Количество конфет на столе: {candys}')
    match status:
        case 1: 
            drag = 20
            print(f'Ход Бота, конфет взято => {drag}')
            status = 5
        case _: 
            drag = int(input('Ход Игрока, берите конфеты => '))
            if drag < 20: status = 2
            elif drag == 20: status = 3
            else: status = 4
    candys -= drag
    turn += 1

    while candys != 0:
        print()
        print(f'Количество конфет на столе: {candys}')

        if turn % 2 != 0: 
            drag = int(input('Ход Игрока, берите конфеты => '))
        else:
            match status:
                case 2:
                    drag = 20 - drag
                    status = 5
                case 3:
                    if drag == 20:
                        drag = 29 - drag
                    elif drag < 20:
                        status = 2
                        continue
                    else: 
                        status = 4
                        continue
                case 4:
                    drag = 49 - drag
                    status = 5
                case 5:
                    drag = 29 - drag
            print(f'Ход Бота, конфет взято => {drag}')
        if (drag > 28) or (drag < 1): 
            print('За раз можно взять от 1 до 28 конфет!!!')
            continue
        if (drag > candys) and (candys < 28):
            print('На столе нет столько конфет!!!')
            continue
        candys -= drag
        turn += 1
    else:
        if turn % 2 == 0: print('Игра окончена. Все конфеты получает Игрок')
        else: print('Игра окончена. Все конфеты получает Бот')

    # 1. Игрок против Игрока
# game_2021_candy_pvp(candy_number)

    # a) Игрок против Бота
# game_2021_candy_pve(candy_number)

    # b) Игрок против "умного" Бота
game_2021_candy_pve_smart(candy_number) 