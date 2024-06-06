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
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(space in ['X', 'O'] for space in board)

def minimax(board, is_maximizing):
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = str(i + 1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = str(i + 1)
                best_score = min(score, best_score)
        return best_score

def play_computer(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def tic_tac_toe():
    while True:
        choice = input('Welcome to TicTacToe\n1. Human vs Human\n2. Human vs Computer\n3. Exit\nPick an option (1, 2, 3): ')
        if choice not in {'1', '2'}:
            break
        
        board = [str(i+1) for i in range(9)]
        current_player = 'x'
        game_ongoing = True

        while game_ongoing:
            print_board(board)
            if choice == '1' or (choice == '2' and current_player == 'x'):
                try:
                    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                    clear_screen()
                    if move < 0 or move > 8 or board[move] in ['X', 'O']:
                        raise ValueError
                except ValueError:
                    clear_screen()
                    print("Invalid move! Please try again.")
                    continue
            else:
                move = play_computer(board)
                clear_screen()

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
