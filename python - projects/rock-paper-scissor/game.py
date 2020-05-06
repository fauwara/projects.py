import random

moves = ['rock','paper','scissor']

combo_dict = {('rock','paper') : False, 
('rock','scissor') : True,
('paper','rock') : True,
('paper','scissor') : False,
('scissor','rock') : False,
('scissor','paper') : True 
}

def result(move_player,move_bot):
    if combo_dict[move_player,move_bot]:
        print('> VICTORY!!')
    else:
        print('> DEFEAT!!')

game_status = True
while game_status:
    correct_input_move = False
    while not correct_input_move:
        mov_p = input('What move will you play? \n> ').lower()
        if not mov_p in moves:
            print('Sorry, We din\'t quite get you there ??')
        else:
            correct_input_move = True

    mov_b = random.choice(moves)

    print(f'PLAYER-1 -> {mov_p} v/s {mov_b} <- COMPUTER')

    if mov_b == mov_p :
        print('> DRAW')
    else:
        result(mov_p,mov_b)

    correct_input_exiting = True
    while correct_input_exiting:
        exit_status = input('play again or quit ?? \n> ').lower()
        if exit_status == 'play again':
            game_status = True
            correct_input_exiting = False
            print('\n')
        elif exit_status == 'quit':
            game_status = False
            correct_input_exiting = False
            print('\n')
        else:
            print('Sorry, We din\'t quite get you there ??')
            correct_input_exiting = True
