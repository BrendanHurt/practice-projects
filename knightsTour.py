#Knight's Tour

#figure out how to take in execution arguments later
#   put in error checking for a 2x2 grid, since the knight can't move
#   also for sizes below 1x1
boardSize = 8
totalSize = boardSize * boardSize
currentX = 0
currentY = 0
currentStep = 0 # tracks the progress through the board
notVis = -1 # value of board spaces that haven't been visited yet

#set space to -1 to make checking if a spot has been visited easier
board = [[notVis for x in range(boardSize)] for y in range(boardSize)]


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
    print(curStep, totalSize) #remove later
    if curStep < totalSize:
        #------------------------------------
        #search down
        if curX + 2 < boardSize:
            print(curStep, "checking down")
            #search left
            if curY - 1 >= 0:
                print(curStep, "checking down-left")
                if board[curX + 2][curY  - 1] == notVis:
                    recurse(curX + 2, curY - 1, curStep + 1)

            #search right
            if curY + 1 < boardSize:
                print(curStep, "checking down-right")
                if board[curX + 2][curY + 1] == notVis:
                    recurse(curX + 2, curY + 1, curStep + 1)
        #------------------------------------
        #search right
        if curY + 2 < boardSize:
            print(curStep, "checking right")
            #search up
            if curX - 1 >= 0:
                print(curStep, "checking right-up")
                if board[curX - 1][curY + 2] == notVis:
                   recurse(curX - 1, curY + 2, curStep + 1)

            #search down
            if curX + 1 < boardSize:
                print(curStep, "checking right-down")
                if board[curX + 1][curY + 2] == notVis:
                    recurse(curX + 1, curY + 2, curStep + 1)
        #------------------------------------
        #search up
        if curX - 2 >= 0:
            print(curStep, "checking up")
            #search left
            if curY - 1 >= 0:
                print(curStep, "checking up-left")
                if board[curX - 2][curY - 1] == notVis:
                    recurse(curX - 2, curY - 1, curStep + 1)

            #search right
            if curY + 1 < boardSize:
                print(curStep, "checking up-right")
                if board[curX - 2][curY + 1] == notVis:
                    recurse(curX - 2, curY + 1, curStep + 1)
        #------------------------------------
        #search left
        if curY - 2 >= 0:
            print(curStep, "checking left")
            #search up
            if curX - 1 >= 0:
                print(curStep, "checking left-up")
                if board[curX - 1][curY - 2] == notVis:
                    recurse(curX - 1, curY - 2, curStep + 1)

            #search down
            if curX + 1 < boardSize:
                print(curStep, "checking left-down")
                if board[curX + 1][curY - 2] == notVis:
                    recurse(curX + 1, curY - 2, curStep + 1)
        #------------------------------------
        #reset the board space & recurse back up
        #else:
            #board[curX][curY] = notVis

    



#print empty board (probably remove later)
for row in board:
    print(row)
print(" ") #just to make a new line

board[0][0] = 0 #change to make any start point available later?
tour(currentX, currentY, currentStep)

for row in board:
    print(row)
