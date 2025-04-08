
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

"""
BASECASE

if we're at the bottom right
    return score

RECURSIVE CASE

1)Find first occurrence of a B or W <- Determines current player
2) Recursively go across the row to find how long the Top row of a perimeter is
3) Check the next row to see if its a middle row and count the empty spaces if it is
4)The next row is either a top row or a middle row and just repeat (2 and 3)
5) after you find a perimeter and have scored it, flip back to 1) but start where the perimeter ends and start over from 1)
"""
def scoreGame(board,current_player,score,x,y):
    if x == len(board)-1 and y == len(board[0])-1:
        return score
   
    if board[x]=="B" or "W":
        board[x]=board[x+1]


    if board[x][y]== "B":
        scoreGame(board,current_player,score,x+1,y)
        scoreGame(board,current_player,score,x,y+1)
    if board[x][y]== "W":
       
def switchPlayer(current_player):
    return 'W' if current_player == 'B' else 'B'



def floodfill(x,y, color , visited, board):
    # check for the out of bounds
    # check for already visitied
    # found a dot
    # diff color
    if x < 0 or x>= len(board) or y < 0 or y >= len(board[0])

    if (x,y) is  visited:
        return True
    # TODO NEED SOMTHIG BETWEEN THE RETURN AND THTE BOOL like a group of the stuff
    if board[x][y] == '.':
        return True  # a dot

    if board[x][y] != color:
        return False  # dif color






   
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
