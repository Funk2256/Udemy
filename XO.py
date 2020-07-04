xx = 'X'
oo = 'O'
start_sim = ''
game_place = f'===========\n {start_sim} | {start_sim} | {start_sim} \n---------\n {start_sim} | {start_sim} | {start_sim} \n===========\n {start_sim} | {start_sim} | {start_sim} \n==========='
def game_start():

    print('XO')
    print('Правила игры: крестики-нолики.....')
    print('Player 1 - ставит X\nPlayer 2 - ставит O\nНачинает Player 1\n:')



count = 0


def game_process(count, game_place):

    while True:
        input_number = int(input())
        if count < 9:
            print(f'Введите число от 0 до 8,  {input_number}')
            count += 1

            if count % 2 == 0: # Проверка на чёт/нечет для определения игроков
                print('Player1: ')

            else:
                print('Player2: ')
            continue

        else:
            print('Game over')
            break

print(game_place)
game_start()
game_process(count, game_place)
