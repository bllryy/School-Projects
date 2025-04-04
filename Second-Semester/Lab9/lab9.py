"""
Henry Lynch, Dylan Mellendick, Marcus Kozlowski, Fin Goscha, & Jaylen Clemons

Lab 8
"""

"""
loadBoard form file
check the board given if it is correct (scoreGame())
    check for all the black and white groups
    and groups with no liberties
    count the territory
    return the final score/ winner

"""


def loadBoard(filename,board):
    with open(filename, 'r') as file:
        board = [list(line.strip()) for line in file if line.strip()]
    return board



def scoreGame(board,current_player,score,x,y):
    white_score = 0
    black_score = 0

    # go with linear search or a bfs solution
    for i in range(len(board)):
        for j in range(len(board[0])):
            if space == 'B':
                black_score += 1
            elif cell == 'W':
                white_score += 1
            elif cell == '.':
                # check for the spaces around the current pos1

    



def printBoard(board):
    for row in board:
        print("", end="")
        for char in row:
            print(char, end= "")
        print()

def main():
    BOARD=loadBoard("testcase1")
    printBoard(BOARD)

    







if __name__ == "__main__":
    main()

