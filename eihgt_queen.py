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

def setQueen(board, rowIndex):
    size = len(board)
    print rowIndex
    if  size - 1 < rowIndex:
        return board
    col = board[rowIndex]
    colIndex = 0
    boards=[]
    for val in col:
        if val == NONE:
            newBoard = deepcopy(board)
            newBoard[rowIndex][colIndex] = PUT_QUEEN
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, 0, lambda setIndex, size : True)
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, 1, lambda setIndex, size : setIndex < size)
            showboard(newBoard)
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, -1, lambda setIndex, size : -1 < setIndex)
            #if rowIndex == 0 :
                #showboard(newBoard)
            boards.append(setQueen(newBoard, rowIndex + 1))
        colIndex = colIndex + 1 
    return boards
            
def checkCantPut(rowIndex, preColIndex, board, thread, condition):
    if len(board) - 1 < rowIndex :
        return board
    index= preColIndex + thread
    print index
    if condition(index, len(board)):
        board[rowIndex][index] = CANT_PUT
        showboard(board)
        return checkCantPut(rowIndex+1, index, board, thread , condition)
    return board

    
board = getBoard(NONE,8)
setQueen(board, 0)

