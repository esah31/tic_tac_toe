# step 1: Setting Up the Board

# Initialize an empty tic-tac-toe board
board = [
    ['','',''], # First row of the board
    ['','',''], # Second row of the board
    ['','',''], # Third row of the board
]

# Step 2: Printing the Board

def print_board(board):
    """
    Print the current state of the tic-tac-toe board.
    """
    for row in board:
      # Print each row of the board
      print("|".join(row))  # Join the elements of the row with '|' and print
      print("-"*5)          # Print a line of dashes to separate rows

# Testing the print_board function
print_board(board)

def make_move(board, row, col, player):
    """
    Place the player's mark on the specified position of the board

    Args:
    - board (list of lists): The current state of the tic-tac-toe board
    - row (int): The row number (0, 1, or 2)
    - col (int): The column number (0,1, or 2)
    - player (str): The player's mark ('X' or 'O')
    """
    board[row][col] = player # Update the specified cell with the player's mark

    make_move(board, 1, 1, 'X')

def check_win(board, player):
    
    """
    Check if the specified player has won the game.

    Args:
    - board (list of lists): The current state of the tic-tac-toe board
    - player (str): The player's mark ('X' or 'O')

    Returns:
    - bool: True if the player has won, False otherwise
    """

    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True  # Player has three marks in a row
        if all(board[j][i] == player for j in range(3)):
            return True  # Player has three marks in a column
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True  # Player has three marks in the main diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True  # Player has three marks in the anti-diagonal
    return False  # No winning combination found

def check_draw(board):
    
    """
    Check if the game has ended in a draw.

    Args:
    - board (list of lists): The current state of the tic-tac-toe board

    Returns:
    - bool: True if the game has ended in a draw, False otherwise
    """

    # Check if any cell on the board is empty
    return all(cell != ' ' for row in board for cell in row)

def get_move(board):
    """
    Prompt the current player to enter their move (row and column numbers).

    Args:
    - board (list of lists): The current state of the tic-tac-toe board

    Returns:
    - tuple: The row and column numbers entered by the player
    """
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            # Check if the selected cell is empty
            if board[row][col] == ' ':
                return row, col  # Return the valid row and column numbers
            else:
                print("That cell is already occupied. Try again.")
        except ValueError:
            print("Please enter a valid integer.")
        except IndexError:
            print("Row and column numbers should be between 0 and 2.")

# Testing the get_move function
row, col = get_move(board)
print(f"Player selected row {row} and column {col}.")
