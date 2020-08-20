from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    
    print('   |   |      ')
    print('{}  | {} | {} '.format(board[7],board[8],board[9]))
    print('   |   |      ')
    print('-----------')
    print('   |   |      ')
    print('{}  | {} | {} '.format(board[4],board[5],board[6]))
    print('   |   |      ')
    print('-----------')
    print('   |   |      ')
    print('{}  | {} | {} '.format(board[1],board[2],board[3]))
    print('   |   |      ')
    print("\n\n")
    
    

def choose_first():
    player=random.randint(1,2)
    if player==1:
        return 'player 1'
    else:
        return 'player 2'



def player_input():
    marker=''
    while not(marker=='X' or marker=='O'):
        marker=input('Player 1: Do you want to be X or O? \n').upper()
        if marker=='X':
            return('X','O')
        else:
            return('O','X')


def place_marker(board,position,marker):
        board[position]=marker



def win_check(board, mark):
    if  board[1]==mark and board[2]==mark  and board[3]==mark:
        return mark
    elif board[5]==mark and board[4]==mark and board[6]==mark:
        return mark
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return mark
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return mark    
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return mark
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return mark
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return mark
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return mark
    else:
        return False     



def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Enter number from 1-9\n'))
    return position                           

def computer_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=random.randint(1,10)
    return position  


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True



def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False



def replay():
    
    return input('Do you want to play again? Enter Yes or No: \n').lower().startswith('y')



print('Welcome to TicTacToe !!!!!!\n')


while True:
    board=[' ']*10
    player1_marker='O'
    player2_marker = 'X'
    turn=choose_first()
    print(turn + ' will go first.')
    s=input('Do you want to start the game?? yes or no\n').lower()
    if s=='no':
        game_on=False
    else:
        game_on=True
    
    while game_on:
        
        if turn == 'player 1':
            
            display_board(board)
            position=player_choice(board)
            place_marker(board,position,player1_marker)
            
            if win_check(board,player1_marker):
                display_board(board)
                print('Congratulations! You have won the game!\n')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw \n")
                    break
                else:
                    turn='player 2'
        
        elif turn == 'player 2':
            
            display_board(board)
            position=player_choice(board)
            place_marker(board,position,player2_marker)
            
            if win_check(board,player2_marker):
                display_board(board)
                print('Congratulations!! player 2 won the game!\n')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw \n")
                    break
                else:
                    turn='player 1'
                
    if not replay():
        break
            
                    