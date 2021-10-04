#Knight's Tour

#figure out how to take in execution arguments later
#   put in error checking for a 2x2 grid, since the knight can't move
#   also for sizes below 1x1
boardSize = 8
totalSize = boardSize * boardSize
currentX = 0
currentY = 0
currentStep = 0 # tracks the progress through the board

#set space to -1 to make checking if a spot has been visited easier
board = [[-1 for x in range(boardSize)] for y in range(boardSize)]


#helper function for recursing through the steps of the algorithm
#   mostly to reduce the amount of repeated code, and to make it more readable
def recurse(x, y, step):
    board[x][y] = step
    tour(x, y, step)

#order of checks:
#   down-right & down-left
#   right-up & right-down
#   up-left & up-right
#   left-up & left-down
def tour(curX, curY, curStep):
    #check if the search is done
    if curStep < totalSize:
        #------------------------------------
        #search down
        if curY + 2 < boardSize:
            #search left
            if curX - 1 >= 0:
                if board[curX - 1][curY + 2] < 0:
                    recurse(curX - 1, curY + 2, curStep + 1)

            #search right
            elif curX + 1 < boardSize:
                if board[curX + 1][curY + 2] < 0:
                    recurse(curX + 1, curY + 2, curStep + 1)
        #------------------------------------
        #search right
        elif curX + 2 < boardSize:
            #search up
            if curY - 1 >= 0:
                if board[curX + 2][curY - 1] < 0:
                   recurse(curX + 2, curY - 1, curStep + 1)

            #search down
            elif curY + 1 < boardSize:
                if board[curX + 2][curY - 1] < 0:
                    recurse(curX + 2, curY - 1, curStep + 1)
        #------------------------------------
        #search up
        elif curY - 2 > 0:
            #search left
            if curX - 1 >= 0:
                if board[curX][curY] < 0:
                    recurse(curX - 1, curY - 2, curStep + 1)

            #search right
            elif curX + 1 < boardSize:
                if board[curX][curY] < 0:
                    recurse(curX + 1, curY - 2, curStep + 1)
        #------------------------------------
        #search left
        elif curX - 2 > 0:
            #search up
            if curY - 1 >= 0:
                if board[curX][curY] < 0:
                    recurse(curX - 2, curY - 1, curStep + 1)

            #search down
            elif curY + 1 < boardSize:
                if board[curX][curY] < 0:
                    recurse(curX - 2, curY + 1, curStep + 1)

        #if no options work, go back up (necessary?)
        else:
            return



#print empty board (probably remove later)
for row in board:
    print(row)
print(" ") #just to make a new line

tour(currentX, currentY, currentStep)

for row in board:
    print(row)
