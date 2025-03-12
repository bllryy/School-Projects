"""
Name:
Section:
Description: Template for Lab 6
"""

"""
Scenario: We are to build a Connect 4 game that runs in the terminal.
"""

def drawBoard(board):
    """ Draws the game board correctly. """
    for row in board:
        print("|", end="")
        for char in row:
            print(f"{char if char != ' ' else ' '}", end="|")
        print()
    print("  " + "   ".join(map(str, range(7))))


def switchPlayer(player):
    """ Switches player turn. """
    return 'O' if player == 'X' else 'X'


def dropPiece(board, player, column):
    """ Drops a piece in the chosen column, placing it in the lowest available row. """
    for row in reversed(board):  # Start from the bottom
        if row[column] == " ":  # Find the first empty slot
            row[column] = player
            return True
    return False  # Column is full


def checkWinner(board, player):
    """ Checks all possible win conditions. """
    ROWS, COLUMNS = len(board), len(board[0])

    # Check Horizontal Win
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check Vertical Win
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check Left Diagonal (\) Win
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check Right Diagonal (/) Win
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False


def main():
    ROWS, COLUMNS = 6, 7
    BOARD = [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]  # Empty board

    CURRENT_PLAYER = "X"
    
    while True:
        drawBoard(BOARD)

        # Get valid column input
        while True:
            try:
                column = int(input(f"Player {CURRENT_PLAYER}, select a column (0-6): "))
                if 0 <= column < COLUMNS and dropPiece(BOARD, CURRENT_PLAYER, column):
                    break
                print("Invalid move! Column is full or out of range.")
            except ValueError:
                print("Invalid input! Enter a number between 0 and 6.")

        # Check for a winner AFTER a piece is placed
        if checkWinner(BOARD, CURRENT_PLAYER):
            drawBoard(BOARD)
            print(f"Player {CURRENT_PLAYER} wins!")
            break  # Exit game loop

        CURRENT_PLAYER = switchPlayer(CURRENT_PLAYER)  # Switch turn


if __name__ == "__main__":
    main()
