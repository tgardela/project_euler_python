import timeit

def solution():
    sudoku = getFileFromPath("096_sudoku.txt")
    sudokuGrids = getSudokuGrids(sudoku)

def getSudokuGrids(sudokuList):
    sudokuGrids = []
    for i in xrange(0, len(sudokuList) - 10, 10):
        if not isNumber(sudokuList[i]):
            sudokuGrids.append([sudokuList[i + 1: i + 10]])
    return sudokuGrids

def getFileFromPath(path):
    codes = []
    file = open(path, 'r')
    for line in file:
        codes.append(line.rstrip().replace(' ',''))
    return codes

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__=="__main__":
    start = timeit.default_timer()

    print solution()


    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"
