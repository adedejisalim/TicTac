# To get the board view
import os
import time


def display_board(board):
    print(' ' + board[7] + ' ||' + board[8] + '   ||' + board[9])
    print('   ||    ||')
    print('--------------')
    print(' ' + board[4] + ' ||' + board[5] + '   ||' + board[6])
    print('   ||    ||')
    print('--------------')
    print(' ' + board[1] + ' ||' + board[2] + '   ||' + board[3])
    print('   ||    ||')


# Function for the player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Function for the place marker
def place_marker(board, marker, position):
    board[position] = marker


# To check if someone has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # through the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # through the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # through the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal 1
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal 2


# To determine what player goes first
import random


def choose_first():
    if random.randint(0, 1) == 1:
        return 'Player 2'
    else:
        return 'Player 1'


# Returns a boolean whether a space on the board is free or not
def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# Checks if the whole board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# Asks for a players position and checks whether the position is free
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Enter the position to be filled: (1-9)\n"))
        no_repeat = []
        if position in no_repeat:
            print('This postion has been used.')
        return position


# To restart the game
def replay():
    return input("Do you want to play again? 'YES' or 'No' \n").lower().startswith('y')


# Now, time to use my functions to make this thing
print("          Welcome to tic tac toe!!!")
print("          Have fun playing the game.")
while True:
    the_board = [' '] * 10
    player = player_input()
    player2_marker, player1_marker = player[0], player[1]
    turn = choose_first()
    time.sleep(2)
    print(turn + ' will go first')
    os.system("cls")

    print('          LOADING.')
    time.sleep(1)
    os.system("cls")
    print('          LOADING..')
    time.sleep(1)
    os.system("cls")
    print('          LOADING...')
    time.sleep(1)
    os.system("cls")
    print("          LOADING COMPLETED!!!")
    time.sleep(2)
    pass
    os.system("cls")

    time.sleep(2)
    play_game = input("Are you ready to play? 'YES' or 'NO'\n")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':  # Player 1's turn
            print("Player 1,Take a turn.")
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            os.system("cls")

            # Check for a win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Congratulations player 1!!! You have won the game.")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The match is a draw.")
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn
            print("Player 2,Take a turn.")
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Congratulations player 2!!! You have won the game.")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The match is a draw.")
                    pass
    if not replay():
        break
