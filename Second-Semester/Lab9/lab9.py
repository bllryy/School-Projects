
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


        
def switchPlayer(current_player):
    return 'W' if current_player == 'B' else 'B'

def find_inside(board):
        for x  in range(len(board)):
            for y in range (len(board[0])):
                    if board [x][y] == 'B':
                        if board [x][y+1] == 'B':
                            return [x,y +1 ]
                        if board [y+] [x+1] 
                        

def floodfill(x,y, color , visited, board):
    # check for the out of bounds
    # check for already visitied
    # found a dot
    # diff color
    if x < 0 or x>= len(board) or y < 0 or y >= len(board[0]):
        if (x,y) is  visited:
            return True
        # TODO NEED SOMTHIG BETWEEN THE RETURN AND THTE BOOL like a group of the stuff
        if board[x][y] == '.':
            return True  # a dot
        if board[x][y] != color:
            return False  # dif color
    #two algorithms; one that searches the parameters, the other that searches 
    group = {(x,y)}
    has_dot = False

    

    """
    ALSO A SET COULD WORK
    
    check for all four directions from the current x,y
    collect all connected stones of the same color
    check if any of them have a dot or a liberity

    start with the all four directions d
    calc the neighbors cords n
    then recursively continue from that neighbor
    add to a group of connected stones
    and keep track of weather any part of the whole group as a empty space

    return the group of the connected stones and if they have a empty space
    """
    

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: # hold these here for now might need to change later
        nx, ny = x + dx, y + dy
        new_group, has_no_space = floodfill(nx, ny, color, visited, board)
        group.update(new_group)
        # https://stackoverflow.com/questions/67573293/pygame-tutorial-tank-with-collision-detection
        # https://www.w3schools.com/python/ref_set_update.asp

        #has_no_space = has_no_space or 
    
    return group, has_no_space



    


   
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
    floodfill(0,0)
    print("\nCaptured stones:")
    #print("Black captured", score['W'], "white stones.")
    #print("White captured", score['B'], "black stones.")

    
if __name__ == "__main__":
    main()
