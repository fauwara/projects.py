def draw_grid(grid_pattern):
    print(f'{grid_pattern[0]} | {grid_pattern[1]} | {grid_pattern[2]}')
    print(f'---------')
    print(f'{grid_pattern[3]} | {grid_pattern[4]} | {grid_pattern[5]}')
    print(f'---------')
    print(f'{grid_pattern[6]} | {grid_pattern[7]} | {grid_pattern[8]} \n')

winning_set = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [6,4,2] ]

player_moves = ['X','0']
playagain = True


while playagain:
    move_no = 0
    gameover = False
    grid_pattern = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    count = 0
    draw = True
    draw_grid(grid_pattern)
    empty = False
    game_status = True
    #for count in range(9):
    # Checking if its player 1 or 2 
    while not gameover:
        
        if count > 7:
            gameover = True
        count += 1

        if (move_no+1)%2 == 0:
            player = 1
        else :
            player = 0
        move_no += 1

        # Taking the right player input 
        correct_input = True
        while correct_input:
            correct_int = True
            while correct_int:
                try:
                    player_move = int(input('Where would you like to play your move. (move to be played between [1-9])\n> '))
                    print('\n')
                    correct_int = False
                except ValueError:
                    print('Sorry, Wrong move try again')
            
            
            if player_move > 0 and player_move < 10:
                if grid_pattern[player_move-1] == ' ' :
                    correct_input = False
                else:
                    print('Sorry, this is already ocupied \n')
            else:
                print('Sorry, you are out of the range. Enter a no. between [0-9]. \n')

        grid_pattern[player_move-1] = player_moves[player]    
        draw_grid(grid_pattern)

        for i in grid_pattern:
            if i != ' ':
                not_empty = True
            else:
                not_empty = False
                break

        for i in range(8):
            if grid_pattern[winning_set[i][0]] != ' ':
                if grid_pattern[winning_set[i][0]] == grid_pattern[winning_set[i][1]] and grid_pattern[winning_set[i][0]] == grid_pattern[winning_set[i][2]]:
                    print(f'Player {player+1} is the Winner\n')
                    gameover = True
                elif not_empty:
                    print('DRAW')
                    break

    while game_status:    
        player_playagain = input('Do you want to play again or quit \n> ').lower()
        if player_playagain == 'play again':
            playagain = True
            game_status = False
        elif player_playagain == 'quit':
            playagain = False
            game_status = False
        else:
            print('Sorry, din\'t quite get you.')
        print('\n')
