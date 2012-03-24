def getBoard(size):   
    row=[1 for j in range(size)] 
    board = [row for i in range(size)]
    return board

print getBoard(4)

def check(col,num,size):
    if num==size:
        return
    nextCol=range(size)

    
