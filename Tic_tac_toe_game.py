###Tic-tac-toe game
#init board
#Begin Game
#Check for win
#Check for draw


# init board
def init_board():
    board = [[' ' for x in range(3)] for y in range(3)]
    return board

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
def check_for_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check for draw
def check_for_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Begin Game
def tic_tac_toe():
    board = init_board()
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (type 'exit' to quit):")
        try:
            row_input = input("Row (0, 1, or 2): ").strip()
            if row_input.lower() == 'exit':
                print("Game exited.")
                break
            row = int(row_input)
            col_input = input("Column (0, 1, or 2): ").strip()
            if col_input.lower() == 'exit':
                print("Game exited.")
                break
            col = int(col_input)
            if row not in range(3) or col not in range(3):
                print("Row and column must be between 0 and 2. Try again.")
                continue
            if board[row][col] != ' ':
                print("Spot already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only or 'exit' to quit.")
            continue
        board[row][col] = current_player
        if check_for_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_for_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
        
tic_tac_toe()