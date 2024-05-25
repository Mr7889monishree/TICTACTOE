board = [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Display the board
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Step 3: Check for a winner
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False

# Step 4 & 5: Main game loop and Player's move
current_player = 'X'

while True:
    display_board()
    
    # Ask for player's move
    row = int(input(f"Player {current_player}, choose row (0-2): "))
    col = int(input(f"Player {current_player}, choose column (0-2): "))
    
    # Check if the cell is empty
    if board[row][col] == ' ':
        board[row][col] = current_player
    else:
        print("That cell is already taken. Try again.")
        continue
    
    # Check for a winner or tie
    if check_winner():
        display_board()
        print(f"Player {current_player} wins!")
        break
    elif all(cell != ' ' for row in board for cell in row):
        display_board()
        print("It's a tie!")
        break
    
    # Step 6: Switch players
    current_player = 'O' if current_player == 'X' else 'X'
