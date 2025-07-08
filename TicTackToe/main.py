import random

# Function to print the current game board
def print_board(board):
    for row in board:
        print(" | ".join(row))     # Join row elements with |
        print("-" * 5)             # Print line separator

# Function to check if a player has won
def check_winner(board, player):
    # Check all rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check all columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full (draw)
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to handle player input
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0, 1, 2): "))
            col = int(input(f"Player {player} - Enter column (0, 1, 2): "))

            if board[row][col] == " ":       # Check if the cell is empty
                board[row][col] = player     # Place player's symbol
                break
            else:
                print("Cell already taken. Try again.")
        except:
            print("Invalid input. Please enter numbers between 0 and 2.")

# Function for AI move (chooses a random empty cell)
def ai_move(board, ai):
    print("AI is making a move...")
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = ai

# Main game function
def play_game(vs_ai=False):
    board = [[" " for _ in range(3)] for _ in range(3)]  # Create 3x3 empty board
    current_player = "X"

    while True:
        print_board(board)

        if vs_ai and current_player == "O":
            ai_move(board, "O")    # AI plays as O
        else:
            player_move(board, current_player)

        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch turns
        current_player = "O" if current_player == "X" else "X"

# Ask user to choose game mode
print("Welcome to Tic-Tac-Toe!")
mode = input("Choose mode:\n1. 2 Player\n2. Play vs AI\nEnter 1 or 2: ")

if mode == "1":
    play_game(vs_ai=False)
elif mode == "2":
    play_game(vs_ai=True)
else:
    print("Invalid choice. Please run the game again.")
