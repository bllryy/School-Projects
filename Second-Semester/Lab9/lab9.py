
"""
Henry Lynch, Dylan Mellendick, Fin Goscha, & Jaylen Clemons

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


def loadBoard(filename):
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

"""
# TODO: feeling two for loops to go though every cell on the board
def scoreGame(board,current_player,score,x,y):
    if x == len(board)-1 and y == len(board[0])-1:
        return score
    if board[x][y]== "B":
        scoreGame(board,current_player,score,x+1,y)
        scoreGame(board,current_player,score,x,y+1)
    if board[x][y]== "W":
        pass
"""


"""
While x,y < bottom right of the board
    Find inside 
    Flood Fill
    Reset x,y = 0 

    
Score game
    


"""


        
def switchPlayer(current_player):
    return 'W' if current_player == 'B' else 'B'

def find_inside(board):
        for x  in range(len(board)):
            for y in range (len(board[0])):
                    if board [x][y] == "B" and board[x][y+1] == "B":
                        if board [x+1][y] == "B":
                            if board [x+1][y+1] == '.':
                                return [x+1,y +1, "B"]
                        elif board [x+1] [y-1] == "B":
                            if board [x+1] [y] == '.':
                                return [x+1,y +1, "B"]
                        elif board [x+1] [y+1] == "B":
                            if board [x+1] [y+2] == '.':
                                return [x+1,y+2, "B"]
                    if board [x][y] == "W" and board[x][y+1] == "W":
                        if board [x+1][y] == "W":
                            if board [x+1][y+1] == '.':
                                return [x+1,y+1, "W"]
                        elif board [x+1] [y-1] == "W":
                            if board [x+1] [y] == '.':
                                return [x+1,y +1, "W"]
                        elif board [x+1] [y+1] == "W":
                            if board [x+1] [y+2] == '.':
                                return [x+1,y+2, "W"]
        return ["Done"]



    
def floodfill(matrix, x, y, color):
    #"hidden" stop clause - not reinvoking for "c" or "b", only for "a".
    if matrix[x][y] == ".":  
        matrix[x][y] = color 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y,color)
        if x < len(matrix[x]) - 1:
            floodfill(matrix,x+1,y,color)
        if y > 0:
            floodfill(matrix,x,y-1,color)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1,color)


def countScore(board):
    blackScore= 0
    whiteScore= 0
    for row in board:
        for cell in row:
            if cell == "B":
                blackScore+=1
            if cell == "W":
                whiteScore+=1
    return [blackScore, whiteScore]
def printBoard(board):
    for row in board:
        print("", end="")
        for char in row:
            print(char, end= "")
        print()

def main():
    board = loadBoard("testcase5.txt")
    printBoard(board)
    print("\nBoard after the capture:")
    coords = find_inside(board)
    while coords[0] != "Done":
        floodfill(board, coords[0], coords[1], coords[2])
        coords=find_inside(board)
    printBoard(board)
    score=countScore(board)
    print("Black captured", score[0], "black stones.")
    print("White captured", score[1], "white stones.")
    if score[0] > score[1]:
        print("Black wins")
    elif score[1]> score[0]:
        print("White wins")
    else:
        print("Tie")
    
if __name__ == "__main__":
    main()
