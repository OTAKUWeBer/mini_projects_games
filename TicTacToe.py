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

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'
    game_ongoing = True

    while game_ongoing:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        if move < 0 or move > 8 or board[move] in ['X', 'O']:
            print("Invalid move! The position is either taken or out of range.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_ongoing = False
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_ongoing = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()