
NONE=0
PUT_QUEEN=1
CANT_PUT=2

def getBoard(defaultVal, size):
    col = [defaultVal for j in range(size)] 
    board = [col for i in range(size)]
    return board

def setQueen(board, putNum):
    size = len(board)
    if putNum == size - 1:
        return
    col = board[putNum]
    index = 0
    boards=[]
    for val in col:
        if val == NONE:
            restBoard = board[putNum + 1 : size ]
            checkCantPutLine(index, restBoard)
            restBoard = checkCantPutSkew(index,restBoard)
            # check cant ph
            # call setQueen method
            boards.append()
        index = index + 1 
    return boards
            
def checkCantPutSkew(colIndex, index, restBoard, thread, condition):
    if len(restBoard) < colIndex :
        return restBoard
    col = restBoard[colIndex]
    if condition():
        col[index + thread] = CANT_PUT
        return checkCantPutSkew(colIndex+1, index, restBoard, thread , condition)
    return restBoard

def checkCantPutLine(index, restBoard):
    for col in restBoard:
        col[index]=CANT_PUT
    return restBoard
    
def showBoard(board):
    for row in board:
        print row

board = getBoard(NONE,4)
showBoard(board)
#print setQueen(board, 0)

