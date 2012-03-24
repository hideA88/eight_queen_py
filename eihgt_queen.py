from copy import deepcopy
NONE=0
PUT_QUEEN=1
CANT_PUT=2

def getBoard(defaultVal, size):
    col = [defaultVal for j in range(size)] 
    board = [col for i in range(size)]
    return board
    
def showboard(board):
    print 
    for row in board:
        print row
    print 

def setQueen(board, putNum):
    size = len(board)
    print putNum
    if  size - 1 < putNum:
        return board
    col = board[putNum]
    index = 0
    boards=[]
    for val in col:
        if val == NONE:
            newBoard = deepcopy(board)
            newBoard[putNum][index] = PUT_QUEEN
            newBoard = checkCantPut(putNum + 1, index, newBoard, 0, lambda setIndex, size : True)
            newBoard = checkCantPut(putNum + 1, index, newBoard, 1, lambda setIndex, size : setIndex < size)
            newBoard = checkCantPut(putNum + 1, index, newBoard, -1, lambda setIndex, size : -1 < setIndex)
            #if putNum == 0 :
                #showboard(newBoard)
            boards.append(setQueen(newBoard, putNum + 1))
        index = index + 1 
    return boards
            
def checkCantPut(colIndex, preRowIndex, board, thread, condition):
    if len(board) - 1 < colIndex :
        return board
    index= preRowIndex + thread
    if condition(index, len(board)):
        board[colIndex][index] = CANT_PUT
        return checkCantPut(colIndex+1, index, board, thread , condition)
    return board

    
board = getBoard(NONE,8)
setQueen(board, 0)

