# -*- coding: utf-8 -*-

from copy import deepcopy
NONE=0
PUT_QUEEN=1
CANT_PUT=2
QUEENS=9
def getBoard(defaultVal, size):
    col = [defaultVal for j in range(size)] 
    board = [col for i in range(size)]
    return board

def getPrintRow(row):
    printRow=[]
    for val in row:
        if val == 1:
            printRow.append('*')
        else:
            printRow.append(' ')
    return printRow

def showboard(board):
    for row in board:
        print getPrintRow(row)
    print 

def copyBoard(board):
    newBoard = []
    for row in board:
        newBoard.append(deepcopy(row))
    return newBoard    

def setQueen(board, rowIndex):
    size = len(board)
    col = board[rowIndex]
    colIndex = 0
    boards=[]
    for  val in col:
        if val == NONE:
            newBoard = copyBoard(board)
            newBoard[rowIndex][colIndex] = PUT_QUEEN
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, 0, lambda setIndex, size : True)
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, 1, lambda setIndex, size : setIndex < size)
            newBoard = checkCantPut(rowIndex + 1, colIndex, newBoard, -1, lambda setIndex, size : -1 < setIndex)
            if size - 1 < rowIndex +1:
                boards.append(newBoard)
            else: 
                for ansBoard in setQueen(newBoard, rowIndex + 1):
                    boards.append(ansBoard)
        colIndex = colIndex + 1 
    return boards
            
def checkCantPut(rowIndex, preColIndex, board, thread, condition):
    if len(board) - 1 < rowIndex :
        return board
    index= preColIndex + thread
    if condition(index, len(board)):
        board[rowIndex][index] = CANT_PUT
        return checkCantPut(rowIndex+1, index, board, thread , condition)
    return board

board = getBoard(NONE,QUEENS)
boards = setQueen(board, 0)
print "ans"
for ans in boards:
    showboard(ans)
print len(boards)
