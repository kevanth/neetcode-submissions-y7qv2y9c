class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(0,9):
            rowSet = set()
            for x in range(0,9):
                cell = board[y][x]
                if cell != "." and cell not in rowSet:
                    rowSet.add(cell)
                elif cell !=".":
                    print(x,y)
                    print(cell)
                    return False
                else:
                    continue
        for x in range(0,9):
            colSet = set()
            for y in range(0,9):
                cell = board[y][x]
                print(cell)
                if cell != "." and cell not in colSet:
                    colSet.add(cell)
                elif cell !=".":
                    print(x,y)
                    print(cell + "--")
                    print(colSet)
                    return False
                else:
                    continue
        cordTuple = [(0,1,2),(3,4,5),(6,7,8)]
        for xRange in cordTuple:
            for yRange in cordTuple:
                boxSet = set()
                for x in xRange:
                    for y in yRange:
                        cell = board[y][x]
                        if cell != "." and cell not in boxSet:
                            boxSet.add(cell)
                        elif cell !=".":
                            print(x,y)
                            print(cell + " AA")
                            return False
                        else:
                            continue
        return True