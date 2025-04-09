
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

def find_inside(board, color):
        for x  in range(len(board)):
            for y in range (len(board[0])):
                    if board [x][y] == color:
                        if board [x+1][y] == color:
                            if board [x+1][y+1] == '.':
                                return [x+1,y +1]
                        if board [x+1] [y-1] == color:
                            if board [x+1] [y] == '.':
                                return [x+1,y +1]
                        if board [x+1] [y+1] == color:
                            if board [x+1] [y+2] == '.':
                                return [x+1,y+2]



    
def floodfill(matrix, x, y, color):
    #"hidden" stop clause - not reinvoking for "c" or "b", only for "a".
    if matrix[x][y] == ".":  
        matrix[x][y] = color 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y,color)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y,color)
        if y > 0:
            floodfill(matrix,x,y-1,color)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1,color)


    

def sccoreGame(board):
    pass
   
def printBoard(board):
    for row in board:
        print("", end="")
        for char in row:
            print(char, end= "")
        print()

def main():
    board = loadBoard("testcase.txt")
    
    #score = scoreGame(board)

    print("\nBoard after the capture:")
    printBoard(board)
    coords = find_inside(board, 'B')
    print(board[coords[0]][coords[1]])
    floodfill(board, coords[0], coords[1] , 'B')
    print("\nCaptured stones:")
    printBoard(board)
    #print("Black captured", score['W'], "white stones.")
    #print("White captured", score['B'], "black stones.")

    
if __name__ == "__main__":
    main()
