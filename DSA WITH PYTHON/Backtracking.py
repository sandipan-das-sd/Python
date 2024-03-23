'''
Psedu code
------------

def placequeen(i, board):  # Function definition taking current row index i and the board state
    for each c such that (i, c) is available:  # Loop through each column c where placing a queen at (i, c) is possible
        place queen at (i, c) and update board  # Place a queen at (i, c) and update the board state accordingly
        if i == n - 1:  # If it's the last row (index n-1), meaning all queens are placed
            return True  # Return True, indicating success in placing all queens
        else:  # If it's not the last row
            extendsoln = placequeen(i + 1, board)  # Recursively call placequeen for the next row and update extendsoln
        if extendsoln:  # If extendsoln is True, indicating a successful placement
            return True  # Return True to propagate the success upwards
    else:  # If there are no available columns in this row
        undo this move and update board  # Undo the previous move (remove the queen from (i, c) and update the board)
else:  # If all columns in this row have been tried but failed
    return False  # Return False, indicating failure to place queens in subsequent rows
    
'''

def placequeen(i, board):
    n = len(board)  # Assuming n is the size of the board (number of rows/columns)

    # Loop through each column c where placing a queen at (i, c) is possible
    for c in range(n):
        # Check if placing a queen at (i, c) is valid (not attacking any other queens)
        if is_safe(i, c, board):
            # Place queen at (i, c) and update board
            board[i][c] = 1

            # If it's the last row (index n-1), meaning all queens are placed
            if i == n - 1:
                return True  # Return True, indicating success in placing all queens
            else:  # If it's not the last row
                # Recursively call placequeen for the next row and update extendsoln
                extendsoln = placequeen(i + 1, board)
                if extendsoln:  # If extendsoln is True, indicating a successful placement
                    return True  # Return True to propagate the success upwards

            # Undo the previous move (remove the queen from (i, c) and update the board)
            board[i][c] = 0

    # If all columns in this row have been tried but failed
    return False  # Return False, indicating failure to place queens in subsequent rows

# Function to check if placing a queen at (row, col) is safe
def is_safe(row, col, board):
    n = len(board)

    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False

    return True

# Example usage:
n = 8  # Size of the chessboard (8x8 in this case)
board = [[0] * n for _ in range(n)]  # Initialize an empty board
placequeen(0, board)  # Start placing queens from the first row
