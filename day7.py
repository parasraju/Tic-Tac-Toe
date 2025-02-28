def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell in ('X', 'O') for row in board for cell in row)

def get_valid_input():
    while True:
        try:
            user_input = input("Enter your move (row and column, e.g., 1 2): ").strip()
            row, col = map(int, user_input.split())
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input! Enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter two space-separated numbers between 0 and 2.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, it's your turn.")
        
        row, col = get_valid_input()
        
        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins! 🎉")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw! 🤝")
                break
            turn += 1
        else:
            print("Invalid move! Cell already occupied. Try again.")
def get_valid_input():
    while True:
        try:
            user_input = input("Enter your move (row and column, e.g., 1 2): ").strip()
            row, col = map(int, user_input.split())
            row -= 1  # Adjust for 1-based indexing
            col -= 1  
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input! Enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter two space-separated numbers between 1 and 3.")

if __name__ == "__main__":
    tic_tac_toe()