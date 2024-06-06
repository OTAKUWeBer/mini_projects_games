import random
import os
import subprocess

def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.run(['cls'], shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.run(['clear'])

def print_board(board):
    board_skeleton = """
{} | {} | {}
---------
{} | {} | {}
---------
{} | {} | {} 
"""
    print(board_skeleton.format(*board))

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def check_draw(board):
    return all(space in ['X', 'O'] for space in board)

def play_computer(board):
    available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
    return random.choice(available_moves)

def tic_tac_toe():
    while True:
        choice = input('Welcome to TicTacToe\n1. Human vs Human\n2. Human vs Computer\n3. Exit\nPick an option (1, 2, 3): ')
        if choice not in {'1', '2'}:
            break
        
        board = [str(i+1) for i in range(9)]
        current_player = 'X'
        game_ongoing = True

        while game_ongoing:
            print_board(board)
            if choice == '1' or (choice == '2' and current_player == 'X'):
                try:
                    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                    if move < 0 or move > 8 or board[move] in ['X', 'O']:
                        raise ValueError
                    clear_screen()
                except ValueError:
                    clear_screen()
                    print("Invalid move! Please try again.")
                    continue
            else:
                move = play_computer(board)

            board[move] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!\n")
                game_ongoing = False
            elif check_draw(board):
                print_board(board)
                print("It's a draw!\n")
                game_ongoing = False
            else:
                current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    tic_tac_toe()
